clear
N=10; sum=0.182; sumr=0.182;
% Number of significant digits in computations
dig=3;

for i=1:N
  sumr=(1/i)-(5*sumr);
  z(i)=sumr;

% additions with dig significant digits
  sum=radd(1/i,-5*sumr,dig);
  y(i)=sum;
end
sumr
'i     Sum    Sum(approx)'
res=[[1:1:N]' z' y']

figure()
hold off
a=plot(y,'b'); set(a,'LineWidth',2);
hold on
a=plot(z,'r'); set(a,'LineWidth',2);
a=plot(abs(z-y)./z,'g'); set(a,'LineWidth',2);
legend([ num2str(dig) ' digits'],'Exact','Error');
grid on
title('Integral of x^n/(x+5) using forward recurrence relation')


N=10; sum=1/(N*6); sumr=1/(N*6);
% Number of significant digits in computations
dig=3;
z=[]; y=[];
for i=1:N-1
  sumr=(0.2/i)-(0.2*sumr);
  z(i)=sumr;

% additions with dig significant digits
  sum=radd(0.2/i,-0.2*sumr,dig);
  y(i)=sum;
end
sumr
'i     Sum    Sum(approx)'
res=[[N-1:-1:1]' z' y']

figure()
hold off
a=plot(y,'b'); set(a,'LineWidth',2);
hold on
a=plot(z,'r'); set(a,'LineWidth',2);
a=plot(abs(z-y)./z,'g'); set(a,'LineWidth',2);
legend([ num2str(dig) ' digits'],'Exact','Error');
grid on
title('Integral of x^n/(x+5) using backward recurrence relation')