library(tidyverse)

args <- commandArgs(trailingOnly=T)
path <- read_lines(args[1])
final <- read_tsv(path[1], col_names=F)

for (file in path[-1]) {
  initial <- read_tsv(file, col_names=F)
  final <- inner_join(final, initial, by=names(final)[1])
}

write_tsv(final, col_names=F, stdout())

