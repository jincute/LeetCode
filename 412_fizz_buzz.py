class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if n == 0:
            return None
        li = [x for x in range(1,n+1)]
        for j in range(n):
            i = j+1
            if i%3==0 and i%5==0:
                li[j] = 'FizzBuzz'
            elif i%3 == 0 and i%5!=0:
                li[j] = 'Fizz'
            elif i%3 != 0 and i%5 == 0:
                li[j] = 'Buzz'
            else:
                li[j] = str(i)
        return li