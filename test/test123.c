#include <stdio.h>


void fun1(unsigned x, unsigned y, unsigned *xyh, unsigned *xyl) {

   unsigned check_negative = 1;

   if (x > 0x80000000) {
      check_negative = check_negative * - 1;
      x = 0xffffffff - x + 1;
   }
   
   if (y > 0x80000000) {
      check_negative = check_negative * - 1;
      y = 0xffffffff - y + 1;
   }

   unsigned xh = x >> 16; 
   unsigned xl = x & 0x0000ffff; 
   unsigned yh = y >> 16; 
   unsigned yl = y & 0x0000ffff;
   unsigned xlyl = xl * yl; 
   unsigned xhyl = xh * yl;
   unsigned xlyh = xl * yh;
   unsigned xhyh = xh * yh;
   unsigned xyl_tmp, xyll;

   unsigned carry = 0;

   xyl_tmp = xlyl + (xhyl << 16);
   if ((xyl_tmp < xlyl) || (xyl_tmp < (xhyl << 16))) {
      carry++;
   }
   
   xyll = xyl_tmp + (xlyh << 16);
   if ((xyll < xyl_tmp) || (xyll < (xlyh << 16))) {
      carry++;
   }
   
   unsigned xyhh = xhyh + (xhyl >> 16) + (xlyh >> 16) + carry;

   if (check_negative == -1) {
      *xyl = 0xffffffff - xyll + 1;
      *xyh = 0xffffffff - xyhh;
   }
   
   else {
      *xyl = xyll;
      *xyh = xyhh;
   }
}


void fun3(unsigned x, unsigned y, unsigned *result)
{
   unsigned valx = 5;
   unsigned valy = 5;
   unsigned res;
   unsigned sign, exp, man;
   
   unsigned xs = (x & 0x80000000) >> 31;
   unsigned xman = ((x << 9) >> 9) & 0x007fffff;
   unsigned xexp =  (x & 0x7f800000) >> 23;
   
   unsigned ys = (y & 0x80000000) >> 31;
   unsigned yman = ((y << 9) >> 9) & 0x007fffff;
   unsigned yexp = (y & 0x7f800000) >> 23;
   
   //   printf("sign of x: %x, y: %x\n", xs, ys);
   //   printf("mantissa of x: %x, y: %x\n", xman, yman);
   //   printf("exponent of x: %x, y: %x\n", xexp, yexp);
   
   if (xexp == 0x00) {
      if (xman == 0x000000) valx = 0; 
          //zero input
   }
   else if (xexp == 0xFF) {
      if (xman == 0x000000) valx = 1; // infinity input
      else valx = 2; // NaN
   }
   else valx = 3; // biased exponent, normalized input
   
   
   if (yexp == 0x00) {
      if (yman == 0x000000) {
         valy = 0; 
         } //zero input
   }
   else if (yexp == 0xFF) {
      if (yman == 0x000000) valy = 1; // infinity input
      else valy = 2; // NaN
   }
   else valy = 3; // biased exponent, normalized input
   
   
   if (valx == 0 || valy == 0) { // zero input
      //printf("제로인풋\n");
      if (valx == 0 && valy !=0) res = y;
      else if (valx != 0 && valy == 0) res = x;
      else if (valx == 0 && valy == 0) {
         if (xs < ys) sign = xs;
         else if (xs > ys) sign = ys;
         else sign = xs;
         res = ((x & 0x7fffffff) | (sign << 31));
      }
      //printf("zerozerozero\n");
      *result = res;
      return;
   }
   
   else if (valx == 1 || valy == 1) { // infinity input
      //printf("인피니티 인풋");
      if (valx == 1 && valy != 1) res = x;
      else if (valx != 1 && valy == 1) res = y;
      else if (valx == 1 && valy == 1) {
         if (xs == ys) res = x;
         else res = 0xffc00000; // NaN
      }
      //printf("beyond the infinity~!~!~!\n");
      *result = res;
      return;
   }
   
   else if (valx == 2 || valy == 2) { // NaN input
      //printf("난 인풋");
      if (valx == 2 && valy != 2) res = (x | 0x7fc00000);
      else if (valx != 2 && valy == 2) res = (y | 0x7fc00000);
      else if (valx == 2 && valy == 2) res = (y | 0x7fc00000);
      //printf("nannanan\n");
      *result = res;
      return;
      }
      
   else if (valx == 3 && valy == 3) {
      printf("여기로 들어가네\n");
   }
   //printf("xman : %x, yman: %x\n", xman, yman);
   
   
   
   sign = xs ^ ys;
   //exp = xexp + yexp -0x7e;
   exp = 127 + (128-xexp) + (128-yexp);
   printf("x : %x\n",x);
   
   printf("xexp: %x, yexp: %x, exp: %x\n", xexp, yexp, exp);
   printf("xman: %x, yman: %x\n", xman, yman);
   
   if (exp >= 0x000000ff) exp = 0xff;
   else if (exp > 0x800000fe) exp = 0x00;
   
   unsigned manh, manl; 
   xman = (xman & 0x00ffffff) | 0x00800000;
   yman = (yman & 0x00ffffff) | 0x00800000;
   fun1(xman, yman, &manh, &manl);
   printf("manh: %x, manl: %x\n", manh, manl);

   //man = (manh & 0x7fffffff) >> 1;
   //man = (manh >> 1);
   while ( manh <= 0x800000)
   {
      manh = manh <<1;
   }

   man = manh | 0x800000;
   printf("man: %x, manh: %x, manl: %x\n", man, manh, manl);
   
   
   man = (man & 0x007fffff);
   res = (man | ((exp << 23) & 0x7f800000));

   res = ((res & 0x7fffffff) | ((sign & 0x00000001)  << 31));

   //printf("result: %f\n", res);
   /*
   unsigned specialcase;
   unsigned gud, val, stck, subtr, roundf;
   gud = (man & 0x00000003);
   val = gud + stck;
   if ((val == 2) && (gud == 1)) val = 1;
   else if ((val == 3) && (gud == 3)) val = 4;

   roundf = val;
   */

   *result = res;


   printf("%08x %08x %08x \n", xman, yman, res);
   return;

}

int main()
{
    /* You can test your implementations through followings*/
   int x, y, xyh=0, xyl=0;
   float f1, f2, f3, result_add, result_mult;

   
   //printf("Problem#1 ");
   //printf("x y ? ");
   //fflush(stdout);
   //scanf("%d %d", &x, &y);
   //fun1((unsigned)x, (unsigned)y,
   //        (unsigned*)&xyh, (unsigned*)&xyl);

   /* the follwing outputs should be same */
   //printf("result#1 0x%08x%08x 0x%016llx\n", xyh, xyl, (long long int)x*y);

   printf("Problem#3 ");
   printf("f1 f2 ? ");
    fflush(stdout);
   scanf("%f %f", &f1, &f2);
   fun3(*(unsigned*)&f1, *(unsigned*)&f2, (unsigned*)&result_mult);

   /* the follwing outputs should be same */
   printf("result#3 %8.5f %8.5f\n", result_mult, f3=f1*f2);

   return 0;
}