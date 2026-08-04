bash --posix
echo "$SHELLOPTS" | grep -o posix # if the word 'posix` does not litera][y print --> u r not in unix because this also means u r not running in posix mode!/bin/sh

my_array=(one two three)
for item in ${my_array[@]}
do
  echo $item
done

