using System.Collections.Generic;
using MyInterpreter_CSharp.domain.adt;

namespace MyInterpreter_CSharp.domain.expression
{
    public class ArithmeticExpression : Expression
    {
        private Expression _e1;
        private Expression _e2;
        private char _op;

        public ArithmeticExpression(Expression e1, Expression e2, char op)
        {
            if (op != '+' && op != '-' && op != '*' && op != '/' && op != '%')
                throw new ExpressionException("Invalid operator.");
            _e1 = e1;
            _e2 = e2;
            _op = op;
        }


        public override int Eval(IMyDictionary<string, int> symbolTable)
        {
            if (_op == '+')
                return _e1.Eval(symbolTable) + _e2.Eval(symbolTable);
            if (_op == '-')
                return _e1.Eval(symbolTable) - _e2.Eval(symbolTable);
            if (_op == '*')
                return _e1.Eval(symbolTable) * _e2.Eval(symbolTable);
            if (_e2.Eval(symbolTable) == 0)
                throw new ExpressionException("Divide by 0.");
            if (_op == '/')
                return _e1.Eval(symbolTable) / _e2.Eval(symbolTable);
            if (_op == '/')
                return _e1.Eval(symbolTable) % _e2.Eval(symbolTable);
            return 0;
        }

        public override string ToString()
        {
            return _e1 + "" + _op + "" + _e2;
        }
    }
}