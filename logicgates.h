#ifndef LOGICGATES_H
#define LOGICGATES_H


#define false 0
#define true !false

int buffer_value(void);
void buffer(int*);
void inverter_pointer(int*);
int inverter_value(int);
int AND_two(int,int);
int AND_three(int,int,int);
int AND_four(int,int,int,int);
int OR_two(int,int);
int OR_three(int,int,int);
int OR_four(int,int,int,int);
int NAND_two(int,int);
int NAND_three(int,int,int);
int NAND_four(int,int,int,int);
int NOR_two(int,int);
int NOR_three(int,int,int);
int NOR_four(int,int,int,int);
int XOR_two(int,int);
int XOR_three(int,int,int);
int XOR_four(int,int,int,int);
int XNOR_two(int,int);
int XNOR_three(int,int,int);
int XNOR_four(int,int,int,int);

int buffer_valuedee(void)
{
    return true;
}

void buffer(int* num)
{
    *num = true;
}

void inverter_pointer(int* num)
{
    if(* num == true)
        * num = false;

    else
        * num = true;
}

int inverter_value(int num)
{
    inverter_pointer(&num);

    return num;
}

int AND_two(int num,int num1)
{
    if(num * num1 == false)
        return false;

    else
        return true;
}

int AND_three(int num,int num1,int num2)
{
    if(AND_two(num,num1) * num2 == false)
        return false;

    else
        return true;
}

int AND_four(int num,int num1,int num2,int num3)
{
    if(AND_three(num,num1,num2) * num3 == false)
        return false;

    else
        return true;
}

int OR_two(int num,int num1)
{
    if(num + num1 == false)
        return false;

    else
        return true;
}

int OR_three(int num,int num1,int num2)
{
    if(OR_two(num,num1) + num2 == false)
        return false;

    else
        return true;
}

int OR_four(int num,int num1,int num2,int num3)
{
    if(OR_three(num,num1,num2) + num3 == false)
        return false;

    else
        return true;
}

int NAND_two(int num,int num1)
{
    return inverter_value(AND_two(num,num1));
}

int NAND_three(int num,int num1,int num2)
{
    return inverter_value(AND_three(num,num1,num2));
}

int NAND_four(int num,int num1,int num2,int num3)
{
    return inverter_value(AND_four(num,num1,num2,num3));
}

int NOR_two(int num,int num1)
{
    return inverter_value(OR_two(num,num1));
}

int NOR_three(int num,int num1,int num2)
{
    return inverter_value(OR_three(num,num1,num2));
}

int NOR_four(int num,int num1,int num2,int num3)
{
    return inverter_value(OR_four(num,num1,num2,num3));
}

int XOR_two(int num,int num1)
{
    return AND_two(inverter_value(num),num1) + AND_two(inverter_value(num1),num);
}

int XOR_three(int num,int num1,int num2)
{
    return XOR_two(XOR_two(num,num1),num2);
}

int XOR_four(int num,int num1,int num2,int num3)
{
    return XOR_two(XOR_three(num,num1,num2),num3);
}

int XNOR_two(int num,int num1)
{
    return inverter_value(XOR_two(num,num1));
}

int XNOR_three(int num,int num1,int num2)
{
    return inverter_value(XOR_two(XOR_two(num,num1),num2));
}

int XNOR_four(int num,int num1,int num2,int num3)
{
    return inverter_value(XOR_two(XOR_three(num,num1,num2),num3));
}

#endif
