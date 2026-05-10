#
# https://www.hackerrank.com/challenges/sherlock-and-valid-string
#

s = gets
hash = {}

for i in 0..(s.size-2)
    c = s[i]
    if hash.has_key? c
        hash[c] = hash[c] + 1
    else
        hash[c] = 1
    end
end

sizes = {}

hash.each do |k,v|
    if sizes.has_key? v
        sizes[v] = sizes[v] + 1
    else
        sizes[v] = 1
    end
end

if sizes.size == 1
    puts "YES"
    exit 0
end

if (sizes.size == 2) &&
   (sizes.values[0] == 1 ||
   sizes.values[1] == 1)
    puts "YES"
    exit 0
end

puts "NO"
