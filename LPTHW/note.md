## ex6

下面几行代码演示了'%r'的效果

'%r'多用于调试时的输出

> x = "There are %d types of people." % 10
> binary = "binary"
> do\_not = "don't"
> y = "Those who know %s and those who %s." % (binary, do\_not)
> print "I said: %r." % x
> print "I also said: '%s'." % y

## ex7

下面这段代码利用一个","实现巧妙的换行

> print end1 + end2 + end3 + end4 + end5 + end6,
> print end7 + end8 + end9 + end10 + end11 + end12

## ex12

pydoc命令可以用于在命令行查询python文档，在命令行输入以下命令：

> pydoc sys

可以查询sys模块的帮助文档

如果是在windows系统，则输入以下命令：

>python -m pydoc sys

## ex25

在源代码中加上"""comments"""这样的注释，随后就可以在python交互环境中运行help(module\_name)来查看文档注释了（documentation comments)


