from tqdm import tqdm
import string
import xml.etree.ElementTree as ET

def extract_word_frequency(movies, gender_dict, pos_mapping, summary_path, window_size=2):
    """Extract word frequency
    """
    for index, movie in tqdm(movies.iterrows()):
        # search two words of {n., adj., v.} before first name and after last name if possible.
        char2gen = movie.character_names
        wiki_id = movie.wikipedia_id
        for character_name, gender in char2gen.items():
            assert gender == "F" or gender == "M"
            name_list = character_name.split()  # split a name into words, e.g. 'desolation williams' -> 'desolation', 'williams'

            # use corenlp data to get the POS of words in the summary and lemmatize the summary.
            tree = ET.parse(summary_path + str(wiki_id) + ".xml")  # use corenlp data
            root = tree.getroot()
            pos_list = root.findall(".//*POS")      # pos of the words
            word_list = root.findall(".//*lemma")   # lemma of the words

            # search forward from the last word of the name and backward from the first word of the name.
            first_name = name_list[0]
            last_name = name_list[-1]
            idx = 0
            length = len(pos_list)
            count_head, count_tail = 0, 0

            # scan the plot and extract all characters mentioned in the characters dataframe.
            while idx < length:
                if (
                    word_list[idx].text.lower() == first_name and 
                    word_list[min(idx + len(name_list) - 1, length - 1)].text.lower() == last_name
                ):
                    head_idx = idx
                    tail_idx = idx + len(name_list) - 1

                    # backward search from the first word of the name.
                    for pre_idx in range(head_idx - 1, -1, -1):
                        if pos_list[pre_idx].text in pos_mapping.keys():
                            # compute word frequency for all words/nouns/verbs/adjectives
                            try:
                                gender_dict[gender]["all"][word_list[pre_idx].text.lower()] += 1
                            except:
                                gender_dict[gender]["all"][word_list[pre_idx].text.lower()] = 1

                            try:
                                gender_dict[gender][pos_mapping[pos_list[pre_idx].text]][word_list[pre_idx].text.lower()] += 1
                            except:
                                gender_dict[gender][pos_mapping[pos_list[pre_idx].text]][word_list[pre_idx].text.lower()] = 1

                            count_head += 1

                        if count_head == window_size:
                            break

                        if word_list[pre_idx].text in string.punctuation:   # don't search across sentences!
                            break

                    # forward search from the last word of the name.
                    for nxt_idx in range(tail_idx + 1, length):
                        if pos_list[nxt_idx].text in pos_mapping.keys():
                            # compute word frequency for all words/nouns/verbs/adjectives
                            try:
                                gender_dict[gender]["all"][word_list[nxt_idx].text.lower()] += 1
                            except:
                                gender_dict[gender]["all"][word_list[nxt_idx].text.lower()] = 1

                            try:
                                gender_dict[gender][pos_mapping[pos_list[nxt_idx].text]][word_list[nxt_idx].text.lower()] += 1
                            except:
                                gender_dict[gender][pos_mapping[pos_list[nxt_idx].text]][word_list[nxt_idx].text.lower()] = 1

                            count_tail += 1

                        if count_tail == window_size:
                            break

                        if word_list[nxt_idx].text in string.punctuation:   # don't search across sentences!
                            break

                    idx = tail_idx + 1

                else:
                    idx += 1

    return gender_dict