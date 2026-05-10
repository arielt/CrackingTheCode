#!/usr/bin/env ruby

# print all permutations of the string

def swap(s, l, r)
  c = s[l]
  s[l] = s[r]
  s[r] = c
  return s
end

def perm(s, l, r)
  if (l == r)
    puts s
  else
    for i in l..r
      swap(s, l, i)
      perm(s, l+1, r)
      swap(s, l, i)
    end
  end
end

s = "abc"
perm(s, 0, s.size-1)
