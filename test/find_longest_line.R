document_content <- readLines("/home/xtarz/course/The-Role-of-Corporate-Culture-in-Bad-Times/data/documents.txt")

longest_line_content <- ""
longest_line_number <- 0


for (identifier in 1:length(document_content)) {
  if (nchar(longest_line_content) < nchar(document_content[identifier])) {
    longest_line_content <- document_content[identifier]
    longest_line_number <- identifier
  }
}


print(longest_line_content)
print(longest_line_number)
print(nchar(longest_line_content))
