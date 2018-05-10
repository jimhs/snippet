#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define MAXOP 100
#define NUMBER '0'
#define BUFSIZE 100
#define MAXVAL 5

char buf[BUFSIZE];
int bufp = 0;

char s[MAXOP];

double val[MAXVAL];
int sp = 0;

int getch(void)
{
	return (bufp>0) ? buf[--bufp] : getchar();
}

void ungetch(int c)
{
	if ( bufp >= BUFSIZE )
		printf("ungetch: too many characters\n");
	else
		buf[bufp++] = c;
}

int getop(char s[])
{
	int i, c;

	while ((s[0]=c=getch()) == ' ' || c == '\t')
		;
	s[1] = '\0';

	if (!isdigit(c) && c != '.')
		return c;
	i=0;
	if(isdigit(c))
		while(isdigit(s[++i] = c = getch()))
			;
	if(c=='.')
		while(isdigit(s[++i] = c = getch()))
			;
	s[i] = '\0';
	if(c != EOF)
		ungetch(c);

	return NUMBER;
}

void push(double f)
{
	if(sp<MAXVAL)
		val[sp++] = f;
	else
		printf("error: stack full, can't push %g\n",f);
}

double pop(void)
{
	if(sp>0)
		return val[--sp];
	else{
		printf("error: stack empty\n");
		return 0.0;
	}
}

int main()
{
	int type;
	double op2;

	while((type=getop(s))!=EOF){
		switch (type){
		case NUMBER:
			push(atof(s));
			break;
		case '+':
			push(pop()+pop());
			break;
		case '*':
			push(pop()*pop());
			break;
		case '-':
			op2 = pop();
			push(pop()-op2);
			break;
		case '/':
			op2 = pop();
			if(op2 != 0.0)
				push(pop()/op2);
			else
				printf("error: zero divisor\n");
			break;
		case '\n':
			printf("\t%.8g\n",pop());
			break;
		default:
			printf("error: unkown command %s\n",s);
			break;
		}
	}
	return 0;
}
