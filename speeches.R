install.packages("rvest")
install.packages("RSelenium")
install.packages("wordcloud")
install.packages("tokenizers")
install.packages("tm")
install.packages("stopwords")
install.packages("ggplot2")
install.packages("dplyr")

library(rvest)
library(wordcloud)
library(tokenizers)
library(tm)
library(stopwords)
library(ggplot2)
library(stringr)
library(RSelenium)
library(sys)

url <- "https://factba.se/transcripts"
rD <- rsDriver(browser = c("firefox"))
remDr <- rD$client
remDr$navigate(url)
before_length = 1
after_length = 0

while(before_length != after_length)
{
  before_length <- length(remDr$findElements(using = "css selector", value ="div[class=\"timeline-panel mediahover\"]"))
  remDr$executeScript("window.scrollTo(0, document.body.scrollHeight)")
  Sys.sleep(5)
  after_length <- length(remDr$findElements(using = "css selector", value ="div[class=\"timeline-panel mediahover\"]"))
  print(c(before_length, after_length))
}
#div_list <- remDr$findElements(using = "css selector", value ="div[class=\"timeline-panel mediahover\"]")
div_list <- speeches$Link
for(div in 1:length(div_list)){
  #speech_url <- unlist(div_list[[div]]$findChildElement(using = "tag name", value = "a")$getElementAttribute("href"))
  speech_url <- div_list[div]
  speech_page <- read_html(speech_url)
  speech_header <- html_text(html_nodes(speech_page, "h1[class=\"topic-page-header transcript-header\"]"))
  speech_date <- str_extract(speech_header, ".?(\\s)?\\w*\\s\\d{1,2}\\s?,?(\\s)?\\d{2,4}.?$")
  speech_type <- str_extract(speech_header,"^.*?(:\\s|\\s-)") 
  speech_title <- trimws(gsub(paste0(c(speech_type, "|", speech_date), collapse = ""), "", speech_header))
  
  speech_date <- trimws(gsub("^-\\s", "", speech_date))
  speech_type <- gsub("(:|-)\\s$", "", speech_type)
  
  speech_div_list <- html_nodes(speech_page, "div[class=\"media topic-media-row mediahover \"]")
  
  #html_text(html_nodes(speech_div_list[1], "div[class=\"speaker-label\"]"))
  speech_text <- paste(html_text(html_nodes(speech_div_list, "a"), trim = "TRUE"), collapse = " ")
  
  if(!exists("speeches")){
    speeches <- as.data.frame(list(speech_title, speech_type, speech_date, speech_url, speech_header, speech_text), 
                              col.names = c("Title", "Type", "Date", "Link", "Header", "Text"))
    speeches$Title <- as.character(speeches$Title)
    speeches$Type <- as.character(speeches$Type)
    speeches$Date <- as.character(speeches$Date)
    speeches$Link <- as.character(speeches$Link)
    speeches$Header <- as.character(speeches$Header)
    speeches$Text <- as.character(speeches$Text)
  } else{
    speeches <- rbind(speeches, list(speech_title, speech_type, speech_date, speech_url, speech_header, speech_text))
  }
  print(speeches[nrow(speeches),-ncol(speeches)])
}
speeches$Date <- gsub(",","", speeches$Date)
speeches$Date <- as.Date(speeches$Date, format="%B %d %Y")

write.table(speeches, file="speeches", sep="|", row.names = FALSE)
speeches2 <- read.table("speeches", header = TRUE, sep = "|", fill = TRUE, quote = "")
names(speeches2) <- names(speeches)
speeches2$Date <-as.Date(speeches2$Date)

rm(speeches)
remDr$close()
rD$server$stop()
# speeches$Date <- as.Date(speeches$Date, format = "%B %d, %Y")
# speeches$Text <- as.character(speeches$Text)

#rD$server$stop()

# page <- read_html(url)
# div_list <- html_nodes(page, "div[class=\"timeline-panel mediahover\"]")
# html_nodes(div_list[1], "a")[2]
# html_text(html_nodes(div_list[1], "a")[1])
# html_attr(html_nodes(div_list[1], "a")[1], "href")
# typeof(html_attr(html_nodes(div_list[1], "a")[1], "href"))

#speech_url <- html_attr(html_nodes(div_list[1], "a")[1], "href")