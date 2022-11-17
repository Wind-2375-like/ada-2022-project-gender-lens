# Gender Analysis on CMU Movie Dataset

***A**ll**D**atapoint**A**ccurate: Yiyang Feng, Naisong Zhou, Haotian Wu, Haolong Li*

## Abstract

As feminist consciousness grows, gender differences in society have received much more attention and people start to wonder where gender differences occur. Movies are a significant player in people's lives. Thus we would like to examine whether gender differences exist in movies. We divide gender differences into gender stereotypes and gender inequalities and analyze how they affect the film itself and the film industry. We will first see whether gender stereotypes exist in movie plot summaries as their influence on movies themselves and figure out how they evolve over time. Then we will tap into the evolutions of gender inequalities from overall gender composition, social networks, and actor careers and make possible explanations in relation to gender stereotypes and social events. After this study, we can gain a deeper understanding of gender difference in films.

## Research Questions

- Do gender stereotypes exist in movie plot summaries and how can we visualize them?
- How does the gender composition among the actors change over time?
- How does gender affect actors' careers in their opportunities and success?
- Is there a structural gender difference in the social networks of actors?

## Proposed Additional Datasets

- [GDP per capita from The World Bank](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD): a dataset containing country names and GDP per capita for analyzing the relationship between the affluence of society and the occurrence of women in the film industry.

## Methods

> ### Do gender stereotypes exist in movie plot summaries and how can we visualize them?

We want to know whether gender stereotypes exist in movie plot summaries. We consider relevant words around male characters and female characters. We implement this by searching plot summaries containing character names in the `character` DataFrame. Then we identify relevant words as the first or last two words of a noun, verb, or adjective from the character name within one sentence. We extract relevant words around these names by gender and count the log frequency of words related to different genders. Finally, we analyze the top 15 frequent words for different genders. We analyze the overall distribution of words describing male and female roles and the distribution of verbs, nouns, and adjectives.

<img alt="图 2" src="https://cdn.jsdelivr.net/gh/Wind2375like/I-m_Ghost/img/cf3913dbcc9499201e620e99d52e04dcaf8e5c61f025b598877efc82f68646f3.png" />

We found that gender stereotypes do exist in movie plot summaries! We can roughly see that males are more related to the words "kill", "police", and "old" while females are associated with the words "love", "marry", and "young". This is a quite primitive analysis and somewhat subjective. We need to refine our analysis and find some methods and metrics in the future.

> ### How does the gender composition among the actors change over time?

text
> ### How does gender affect actors' careers in their opportunities and success?

text

> ### Is there a structural gender difference in the social networks of actors?

text

## Proposed Timeline

- 18 November – 25 November: 
- 25 November – 2 December:
- 2 December –9 December: meeting
- 9 December – 16 December: 准备 meeting
- 16 December – 23 December: 最终 refine story 和 data analysis

## Organization within the Team

<!---
A list of internal milestones up until project Milestone 3.
--->
<table class="tg" style="undefined;table-layout: fixed; width: 342px">
<colgroup>
<col style="width: 164px">
<col style="width: 178px">
</colgroup>
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax">Tasks</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Haolong</td>
    <td class="tg-0lax">Discover regional gender composition in the movie industry<br><br>Discover the relationship between gender composition and factors like major social events or society wealth<br><br>Develop the final text for the data story</td>
  </tr>
  <tr>
    <td class="tg-0lax">Haotian</td>
    <td class="tg-0lax">Build the actor social network to analyze the structual gender difference in the actor relationship<br><br>Develop the web interface for the data story<br><br>Develop the final text for the data story</td>
  </tr>
  <tr>
    <td class="tg-0lax">Naisong</td>
    <td class="tg-0lax">Analyze difference f/m career opportunities through character persona clustering and social analysis<br><br>Discover the relationship between gender and actors' level of success<br><br>Develop the final text for the data story</td>
  </tr>
  <tr>
    <td class="tg-0lax">Yiyang</td>
    <td class="tg-0lax">Develop the web interface<br><br>Process text data from plot summaries<br><br>Analyze gender stereotypes from processed text data<br><br>Develop the final text for the data story</td>
  </tr>
</tbody>
</table>
