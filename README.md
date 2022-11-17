# Gender Analysis on CMU Movie Dataset

_**A**ll**d**atapoint**a**ccurate: Yiyang Feng, Naisong Zhou, Haotian Wu, Haolong Li_

## Abstract

As feminist consciousness grows, gender differences have received much more attention, and people have started to wonder where gender differences occur. Movies are a significant player in people's lives. Thus we would like to examine whether gender differences exist in movies. We divide gender differences into gender stereotypes and gender inequalities and analyze how they affect the film itself and the film industry. We will first see whether gender stereotypes exist in movie plot summaries as their influence on movies themselves and figure out how they evolve. Then we will tap into the evolutions of gender inequalities from overall gender composition, social networks, and actor careers and make possible explanations with gender stereotypes and social events. After this study, we can gain a deeper understanding of gender differences in films.

## Research Questions

- Do gender stereotypes exist in movie plot summaries and how can we visualize them?
- How does the gender composition among the actors change over time?
- How does gender affect actors' careers in their opportunities and success?
- Is there a structural gender difference in the social networks of actors?

## Proposed Additional Datasets

- [GDP per capita from The World Bank](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD): a dataset containing country names and GDP per capita for analyzing the relationship between the affluence of society and the occurrence of women in the film industry.

## Methods

> ### Do gender stereotypes exist in movie plot summaries and how can we visualize them?

We want to know whether gender stereotypes exist in movie plot summaries. We consider relevant words around male characters and female characters. We implement this by searching plot summaries containing character names in character DataFrame. Then we identify relevant words as the first or last two words of a noun, verb, or adjective from the character name within one sentence. We extract relevant words around these names by gender and count the log frequency of words related to different genders. Finally, we analyze the top 15 frequent words for different genders. We analyze the overall distribution of words describing male and female roles and the distribution of verbs, nouns, and adjectives.

<img alt="图 2" src="https://cdn.jsdelivr.net/gh/Wind2375like/I-m_Ghost/img/cf3913dbcc9499201e620e99d52e04dcaf8e5c61f025b598877efc82f68646f3.png" />

We found that gender stereotypes do exist in movie plot summaries! We can roughly see that males are more related to the words "kill", "police", and "old", while females are associated with the words "love", "marry", and "young". The analysis is relatively primitive and subjective. We need to refine our analysis and find some methods and metrics in the future.

> ### How does the gender composition among the actors change over time?

In this section, we are interested in how gender composition evolves and find possible reasons for such variations. To answer these questions, we first derive the annual gender composition in the movie industry.

<img alt="image 5" src="./images/genderDiff.png" />

<img alt="image 6" src="./images/genderRatio.png" />

It is not hard to see that the portion of female actors first decreases then increases, while the absolute number of female actors keeps increasing after around 1942.

We are further interested in the reasons behind those changes. Do major social events like wars and economic crises influence women's occurrence in the movies? Does social wealth (GDP) have something to do with this? To account for these questions, we will need to align historical events and annual GDP to the timeline to see if there are effects. To prove the claims statistically, we will use methods including hypothesis testing and error bars to clarify things.

> ### How does gender affect actors' careers in their opportunities and success?

We raised two sub-questions when investigating how female and male actors differ in their careers: Are female and male actors given equal opportunities in the movie industry? Do they achieve the same level of success?

To answer the first question, we grouped characters by year and see if the total number of female and male actors differs:

<img alt="image 3" src="./images/actor_population_evolution.png" />

We also plot the average age evolution of female and male actors:

<img alt="image 4" src="./images/actor_age_evolution.png" />

The plots above show that: 1. female characters are far fewer than male actors, and the opportunities are not equally given. 2. female actors are generally younger than male actors, meaning that female actors have a shorter career span than male actors. What leads to this phenomenon? We will investigate through 4 main directions: market preference, the social influence of actors, stereotypes in movies, and the general lack of opportunities for women in all professions.

To answer the second question, we need first to define success. We will define a function that aggregates both revenues actors made and their industrial influence based on the following discussed social network, which is to be implemented and refined afterwards.

> ### Is there a structural gender difference in the social networks of actors?

Actors are an essential part of the movies, and the movies in which the two actors have worked together can be seen as a direct link between these two actors, which contributes to a vast social network. With the help of such a network structure, we can find the structural gender difference in the movies.

We start to build up the graph with the prepared nodes and edges data. We use `nx.Graph()` to generate an empty undirected graph and load our prepared data. In our social network graph, every actor represents a node and has an edge between two nodes if the two actors cooperate in at least one movie. First, we analyze the Top100 most influential actors' gender and height difference preliminarily and then draw out their social relationship topology. In the next stage, we will consider the attributes of edges in our graph, such as the number of cooperation. We also try to use the Louvain Modularity Algorithm or Girvan-Newman Algorithm to analyze gender differences in the social relationship topology.

<img alt="image 4" src="./images/Top100_Graph.png" width = "50%">

## Environment Setup

Run in the terminal:

```shell
conda env create -f environment.yml
```

## Proposed Timeline

- 18 November – 25 November: Continue the project and conduct a deeper analysis according to the future directions.
- 25 November – 2 December: Pause project work and do the Homework 2.
- 2 December –9 December: Integrate all analysis and write out the draft of our datastory.
- 9 December – 16 December: Complete the team GitHub including all code and other documents, and revise our datastory to the final version.
- 16 December – 23 December: Build the web development interface to tell our datastory.

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
    <td class="tg-0lax">Discover regional gender composition in the movie industry<br><br>Discover the relationship between gender composition and factors like major social events or societal wealth<br><br>Develop the final text for the data story</td>
  </tr>
  <tr>
    <td class="tg-0lax">Haotian</td>
    <td class="tg-0lax">Build the actor social network to analyze the structural gender difference in the actor relationship<br><br>Develop the web interface for the data story<br><br>Develop the final text for the data story</td>
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
