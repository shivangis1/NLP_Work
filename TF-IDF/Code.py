import csv
import string
import math

csv.field_size_limit(1000000000)

with open('state-of-the-union.csv', 'rb') as sotu_file:
    reader = csv.reader(sotu_file)
    sotu_tokenized = {}
    # iterating the CSV file, each row is "year", "speech" (speech is a very long string)
    for row in reader:
        # the year is in row[0]
        year = int(row[0])
	# the whole speech for the year is in row[1]
        speech = row[1]
	# converting all characters to lowercase
        lowercase_speech = speech.lower()
	# removing all punctuation characters
        stripped_punctuation = lowercase_speech.translate(string.maketrans(string.punctuation, " " * len(string.punctuation)))
	# splitting the speech into a list of words
	# sotu_tokenized is a dictionary, the year of the speech is the key, the value is the speech as a list of strings with each word
        sotu_tokenized[year] = stripped_punctuation.split()
        
# tf_list is a dictionary: the key is the year of the speech and the value is tf
tf_list = {}
for year in sotu_tokenized:
    # tf is a dictionary: the key is the word and the value is the frequency of the word in the document
    tf = {} 
    for word in sotu_tokenized[year]:
        tf[word] = tf.get(word, 0) + 1
    tf_list[year] = tf;

# df is a dictionary where the key is word and the value is the
# number of documents it appears
df = {}
for year in tf_list:
    for word in tf_list[year]:
        df[word] = df.get(word, 0) + 1

#idf is the dictionary that contains the words
#along with their idf weights
#idf=log(total no of documents/number of documents word appears in)
idf = {}
number_documents = len(tf_list)
for word in df:
    idf[word] = math.log((number_documents / df[word]), 2)

#tf_idf_list contains the tf-idf vectors for each document
#key is each word and value is product of tf value*idf weight
tf_idf_list = {}
for year in tf_list:
    tf = tf_list[year]
    tf_idf = {}
    for word in tf:
        tf_idf[word] = tf[word] * idf[word]
    tf_idf_list[year] = tf_idf

    
#length is used to calculate the length of the vector
#length=square root(sum of all (tf_idf)^2)
length = {}
for year in tf_idf_list:
    tf_idf = tf_idf_list[year]
    length[year] = 0
    for word in tf_idf:
        length[year] += tf_idf[word] * tf_idf[word]
    length[year] = math.sqrt(length[year])

#tf_idf_list_norm contains the set of normalized vectors
#normalized vectors are obtained by dividing each vector with
#the length obtained in the previous segment
tf_idf_list_norm = {}
for year in tf_idf_list:
    tf_idf = tf_idf_list[year]
    tf_idf_norm = {}
    for word in tf_idf:
        tf_idf_norm[word] = tf_idf[word] / length[year]
    tf_idf_list_norm[year] = tf_idf_norm

#sorted_words_list contains words sorted based on weights
#key is the word and value is its weight
#it is sorted in descending order
sorted_words_list = {}
for year in tf_idf_list_norm:
    tf_idf_norm = tf_idf_list_norm[year]
    sorted_words_list[year] = sorted(tf_idf_norm, key = tf_idf_norm.__getitem__, reverse = True)
        
#prints the top 20 most weighted words for each year from 1960-1970
for year in range(1960, 1971):
    print "\n\nYear = " + str(year) + "\n"
    sorted_words = sorted_words_list[year]
    for i in range(0, 20):
        print sorted_words[i] + "  = " + str((tf_idf_list_norm[year])[sorted_words[i]])

#tf_idf_dec_list is a dictionary that contains
#the decade as the key and value as tf_idf of that decade
tf_idf_dec_list = {}
for decade in range(1900, 2020, 10):
    tf_idf_dec = {}
    for year in range(decade, decade + 10):
        tf_idf_norm = tf_idf_list_norm.get(year, {})
        for word in tf_idf_norm:
            tf_idf_dec[word] = tf_idf_dec.get(word, 0) + tf_idf_norm.get(word, 0)
    tf_idf_dec_list[decade] = tf_idf_dec

#sorted_words_dec_list contains the tf_idf of each decade in a descending order
sorted_words_dec_list = {}
for decade in tf_idf_dec_list:
    tf_idf_dec = tf_idf_dec_list[decade]
    sorted_words_dec_list[decade] = sorted(tf_idf_dec, key = tf_idf_dec.__getitem__, reverse = True)

sorted_decs_list = sorted(sorted_words_dec_list)

print "############################################################"
print "############################################################"
 
#Below iteration prints the top 20 most-weighted terms for each decade
for decade in sorted_decs_list:
    print "\n\nDecade = " + str(decade) + "\n"
    sorted_words_dec = sorted_words_dec_list[decade]
    tf_idf_dec = tf_idf_dec_list[decade]
    for i in range(0, 20):
        print sorted_words_dec[i] + " = " + str(tf_idf_dec[sorted_words_dec[i]])