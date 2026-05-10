#!/usr/bin/env ruby

# print top ranked completions of given word

require 'trie'

words = {
  'n' => 1,
  'no' => 3,
  'no more' => 5,
  'no more tears' => 7
}

t = Trie.new
words.each do |k,v|
  t.add k, v
end

puts "enter a word"
s = gets.chomp
children = t.children_with_values(s)

result = children.sort_by {|v| v[1]}.reverse.first(3)

result.each do |v|
  puts v[0]
end
