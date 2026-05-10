#!/usr/bin/env ruby

# Given a string where in each word letters were randomly shuffled and after
# that words were written without spaces (lets call it X). Also you have a
# dictionary. The task is to return all possible strings S that can be
# transformed into the string X and all words in S are from dictionary.

require 'pp'

# build NF for the word
def sorts(s)
  s = s.chars.sort.join
end

# recursion: find partitions
def rec_s(s, start, prefix, xd, rv)
  for i in start .. s.size - 1
    word = s[start..i]
    sorted = sorts(word)
    if xd.has_key?(sorted)
      new_prefix = prefix.clone << sorted
      if i == s.size - 1
        rv << new_prefix
        return
      else
        rec_s(s, i + 1, new_prefix, xd, rv)
      end
    end
  end
end

# print all possible strings for NF
def print_arr(arr, i, prefix, xd, rv)
  vals = xd[arr[i]]
  vals.each do |v|
    new_prefix = prefix.clone << v
    if i == arr.size - 1
      rv << new_prefix
    else
      print_arr(arr, i+1, new_prefix, xd, rv)
    end
  end
end

# preparation
def alls(s, dict)
  rv = []
  xd = {}

  # build NF dict
  # NF: sorted letters of word
  dict.each do |k,v|
    key = sorts(k)
    if xd.has_key?(key)
      xd[key] << k
    else
      xd[key] = [k]
    end
  end

  # get all posssible NF partitions for the string
  rec_s(s, 0, [], xd, rv)

  # print all posibilities for NF parition
  all = []
  rv.each do |v|
    print_arr(v, 0, [], xd, all)
  end
  return all
end

# driver
dict = {
  "my" => true,
  "car" => true,
  "acr" => true,
  "a" => true,
  "rc" => true
}

s = "ymacr"

puts "String: #{s}"
puts "Dict: #{dict}"
puts "Possible source strings:"
pp alls(s, dict)
