install.packages("rvest")
install.packages("wordcloud")
install.packages("tokenizers")
install.packages("tm")
install.packages("stopwords")
install.packages("ggplot2")

library(rvest)
library(wordcloud)
library(tokenizers)
library(tm)
library(stopwords)
library(ggplot2)

trumpURL <- "https://www.nytimes.com/2019/10/27/us/trump-transcript-isis-al-baghdadi.html"
trumpPage <- read_html(trumpURL)

trump_pList <- html_nodes(trumpPage, "p")
trump_pList <- trump_pList[-c(1:5, 19)]
trump_text <- html_text(trump_pList, trim = TRUE)
trump_text <- paste(trump_text, collapse = " ")

# for(i in 1:length(trump_text))
# {
#   trump_text[i] <- trimws(trump_text[i])
# }


obamaURL <- "https://obamawhitehouse.archives.gov/blog/2011/05/02/osama-bin-laden-dead"
obamaPage <- read_html(obamaURL)

obama_pList <- html_nodes(obamaPage, "p")
obama_pList <- obama_pList[-c(1:6, 31)]
obama_text <- html_text(obama_pList, trim=TRUE)
obama_text <- paste(obama_text, collapse = " ")

# for(i in 1:length(obama_text))
# {
#   obama_text[i] <- trimws(obama_text[i])
# }

windows()
wordcloud(trump_text, scale=c(5, 0.5), random.order=FALSE, 
          colors=brewer.pal(8, "Dark2"), random.color=TRUE, rot.per=0.25,
          min.freq=2, max.words=Inf)

wordcloud(obama_text, scale=c(2, 0.5), random.order=FALSE, 
          colors=brewer.pal(8, "Dark2"), random.color=TRUE, rot.per=0.25,
          min.freq=2, max.words=Inf)

windows(height=6, width=6)
bringToTop(2)
grams_trump <- tokenize_ngrams(trump_text, n = 1, n_min = 1,lowercase=TRUE)#, stopwords = stopwords()[stopwords() != "i"])
sum(table(unlist(grams_trump)))
grams_trump <- tokenize_ngrams(trump_text, n = 3, n_min = 1,lowercase=TRUE, stopwords = stopwords()[stopwords() != "i"])
g_trump <- table(unlist(grams_trump))
g_trump_df <- data.frame(g_trump)
names(g_trump_df) <- c("term", "freq")
wordcloud(words=g_trump_df$term[g_trump_df$freq>1], freq=g_trump_df$freq[g_trump_df$freq>1], scale=c(2, 0.5), random.order=FALSE, 
          colors=brewer.pal(8, "Dark2"), random.color=TRUE, rot.per=0.25,
          min.freq=2, max.words=Inf)
#ggplot(g_trump_df[g_trump_df$freq>2,], aes(term)) + geom_bar(stat="count")


windows(height=6, width=6)
bringToTop(3)
#grams_obama <- tokenize_ngrams(obama_text, n = 1, n_min = 1,lowercase=TRUE)#, stopwords = stopwords()[stopwords() != "i"])
#sum(table(unlist(grams_obama)))
grams_obama <- tokenize_ngrams(obama_text, n = 3, n_min = 1,lowercase=TRUE, stopwords = stopwords()[stopwords() != "i"])
g_obama <- table(unlist(grams_obama))
g_obama_df <- data.frame(g_obama)
names(g_obama_df) <- c("term", "freq")
wordcloud(words=g_obama_df$term[g_obama_df$freq>1], freq=g_obama_df$freq[g_obama_df$freq > 1], scale=c(2, 0.5), random.order=FALSE, 
          colors=brewer.pal(8, "Dark2"), random.color=TRUE, rot.per=0.25,
          min.freq=2, max.words=Inf)
