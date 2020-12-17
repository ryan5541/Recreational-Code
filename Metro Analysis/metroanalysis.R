install.packages("rvest")
library(rvest)
library(readr)
library(ggplot2)

# url <- 'https://www.hstheaterawards.com/winners-and-nominees'
# webpage <- read_html(url)
# x <- html_node(webpage, xpath = '//*[@id="comp-izewwbmy"]/p[3]')
# html_text(webpage)
# webpage

rm(nom)
nom <- read.csv(file = "./awards2017-3.txt", header = FALSE, sep = ",")
nom <- read.csv(file = "./awards2017-4.txt", header = FALSE, sep = ",")

p_17 <- read.csv(file = "./participants2017.txt",header = FALSE, sep = ",")
colnames(p_17) <- c("hs", "show", "county")
p_17$hs <- gsub("[Hh]igh [Ss]chool", "HS", p_17$hs)

colnames(nom) <- c("hs", "blah", "blah2")
View(nom$hs)
nom <- nom[(grepl("[Hh][Ss]|[Hh]igh [Ss]chool", nom$hs) & (!grepl("\\(.*\\)", nom$blah))),]
nom <- nom[,1:2]
nom <- data.frame(nom)
nom$blah <- iconv(nom$blah, to="ASCII", sub="")
nom <- nom[(!duplicated(nom$hs)),]
colnames(nom) <- c("hs")
nom <- merge(nom, p_17[,c(1,3)], by = "hs", all.x = TRUE)
nom$hs <- gsub("Pleasant(i)?ville.*", "Pleasantville HS", nom$hs)
nom[grepl("Saddle.*", nom$hs),]$county <- "Westchester"
nom[grepl("Byram.*", nom$hs),]$county <- "Westchester"
nom[grepl("Carmel.*", nom$hs),]$county <- "Putnam"
nom_16 <- merge(nom, p_16[,c(1,3)], by = "hs", all.x = TRUE)

nom <- data.frame(nom)
nom <- nom[grepl("[Hh][Ss]|[Hh]igh [Ss]chool", nom$hs),]
nom$hs <- gsub("Northern Highlands.*", "Northern Highlands Regional HS", nom$hs)
nom$hs <- gsub("Northern Valley.*", "Northern Valley Regional HS Old Tappan", nom$hs)
nom$hs <- gsub("Rye H.*", "Rye HS", nom$hs)
nom$hs <- gsub("St\\. Joseph.*", "St. Joseph Regional HS", nom$hs)
nom$hs <- gsub("Fair.*", "Fair Lawn HS", nom$hs)

View(nom[is.na(nom$county),])
colnames(nom) <- c("hs")
windows()
summ <- data.frame(table(nom_17$hs))
summ <- summ[grepl("[Hh][Ss]|[Hh]igh [Ss]chool", summ$nom),]
summ_17 <- summ
nom <- merge(nom, p_17, by = "hs", all = TRUE)
colnames(summ_17) <- c("hs", "noms")

View(merge(p_17, summ_17, by = "hs", all.x = TRUE))
sd(summ$Freq)
ggplot(data = nom, aes(x = nom))+
  geom_bar()+
  coord_flip()
