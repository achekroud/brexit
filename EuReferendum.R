library(jsonlite)
library(ggplot2)
library(dplyr)

dir.create("~/brexit")

curl::curl_download(url = "https://petition.parliament.uk/petitions/131215.json",
                    destfile = "~/brexit/euReferendum.json")

original <- fromJSON("~/brexit/euReferendum.json")

raw <- original$data$attributes$signatures_by_constituency

raw %>%
    arrange(-signature_count) %>%
    slice(1:30) %>%
    mutate(mp = factor(mp, levels = mp[order(signature_count)])) %>%
    ggplot(aes(mp, signature_count)) +
    geom_bar(aes(x = mp), stat = "identity") +
    coord_flip() + theme_bw() +
    xlab("MP") + ylab("Number of petitions for 2nd EU Referendum") +
    ggtitle("Top 30 Consituencies by \n re-referendum popularity")
    
    
    
    factor(fig_trails1$SNP,
           levels = fig_trails1$SNP[order(fig_trails1$Importance)])