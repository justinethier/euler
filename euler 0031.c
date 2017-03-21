// "Cute" solution to Project Euler 31
// Also much faster than Python version :)
#define elif else if
const int NCURRENCY = 8, COST = 200,
Currency[] = {1,2,5,10,20,50,100,200};

int find(int ic, int sum)                {
  int coin = Currency[ic], i, ways = 0;
  if (ic >= NCURRENCY) return ways;
  for(i = 0; i < COST/coin + coin; i++){
     int  amt =  sum + i * coin;
      if (amt >  COST) return ways;
    elif (amt == COST) ways++;
    else ways += find(ic + 1, amt);    }
  return ways;                           }

void main(){ printf("%d\n", find(0, 0)); }