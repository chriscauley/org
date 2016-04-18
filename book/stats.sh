echo "md"
find . -name '*.md' | xargs wc -w
echo "org"
find . -name '*.org' | xargs wc -w
