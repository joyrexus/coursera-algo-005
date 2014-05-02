# Divide an array into two sub-arrays
split = (arr) ->
  n = arr.length - 1
  i = Math.round(n / 2)
  [arr[...i], arr[i..]]

# Merge two sorted sub-arrays
merge = (a, b) ->
  n = a.length + b.length
  i = j = 0
  result = []
  for k in [0..n]
    if a[i] < b[j]
      result.push(a[i])
      i += 1
    else
      result.push(b[j])
      j += 1
    if a.length == i
      return result.concat(b[j..])
    else if b.length == j
      return result.concat(a[i..])
  result
  
# Numerically sort an array
sort = (arr) ->
    return arr if arr.length < 2
    [a, b] = split(arr)
    merge(sort(a), sort(b))


# Testing
assert = require 'assert'

input = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

assert.deepEqual sort(input), input.reverse()
