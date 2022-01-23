""" Let y be the year (such as 1800 or 2001 or whatever)
2. Divide y by 19 and call the remainder a. Ignore the
quotient.
3. Divide y by 100 to get a quotient b and a remainder c.
4. Divide b by 4 to get a quotient d and a remainder e.
5. Divide 8 * b +13 by the value 25, to get a quotient g.
Ignore the remainder.
6. Divide 19 * a + b - d - g + 15 by the value 30, to get a
remainder h. Ignore the quotient.
7. Divide c by 4 to get a quotient j, and a remainder k.
8. Divide (a + 11) * h by the value 319, to get a quotient m.
Ignore the remainder.
9. Divide 2 * e + 2 * j - k - h + m + 32 by the value 7 to get a
remainder r. Ignore the quotient.
10. Divide h - m + r + 90 by the value 25, to get a quotient n.
Ignore the remainder.
11. Divide h - m + r + n + 19 by the value 32, to get a
remainder p. Ignore the quotient.

Then Easter falls on day p of month n.  """

def easter():
    y = input("Enter a year: ")
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) // 30
    j = c // 4
    k = c % 4
    m = ((a + 11) * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32

print ("Easter falls on day " + str(p) + "of month " + str(n))












