# Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.

# Note:
# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.

# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']
# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
# beginWord = "hungry"
# endWord = "happy"
# None

from graph import Graph

word_list = []
with open('words.txt', 'r') as wordsfile:
    for word in wordsfile:
        currentWord = word[:-1]
        word_list.append(currentWord)

def differ_by_one(word1, word2):
    different = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            different += 1
    return different <= 1

def shortest_transformation(begin_word, end_word):
    graph = Graph()
    # Loop over word_list and add vertices for words of same length as begin_word
    for word in word_list:
        if len(word) == len(begin_word):
            graph.add_vertex(word)

    # Loop over vertices and create edges
    for word1 in graph.vertices:
        for word2 in graph.vertices:
            if word1 != word2 and differ_by_one(word1, word2):
                graph.add_edge(word1, word2)

    # Use BFS to find shortest path
    return graph.bfs(begin_word, end_word)

print(shortest_transformation('hit', 'cog'))
print(shortest_transformation('sail', 'boat'))