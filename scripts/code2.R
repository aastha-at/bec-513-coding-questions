library(ggplot2)

args <- commandArgs(trailingOnly=T)
output <- args[1]
x_label <- args[2]
y_label <- args[3]
title <- args[4]

data <- read.table(file("stdin"), header=F, sep="\t")
colnames(data) <- c("x", "y", "group")
plot <- ggplot(data, aes(x=x, y=y, color=group, group=group)) +
  geom_line() +
  labs(x=x_label, y=y_label, title=title) +
  theme_minimal()

ggsave(output, plot, width=8, height=6)

