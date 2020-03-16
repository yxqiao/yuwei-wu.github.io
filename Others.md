## stack top 是最后放进来的元素


## 1.布尔运算: and, or, not 
```
X and Y
X or Y
not X
```

## 2.十六进制/二进制／十进制之间的转换
```
# 转为十进制
int('0xf',16) 
int('10100111110',2)      
int('17',8)    
```
```python
# 转十六进制
 hex(1033)
>>>'0x409'
 hex(int('101010',2))
>>>'0x2a'
```
```python
# 转二进制
 bin(10)
>>>'0b1010'
bin(int('17',8))
>>>'0b1111'
```
```python
#oct 函数 可将 任意进制的数 转换成 8进制
oct(0xf) 
>>>'017'
```

## 3.闪存flash memory/ RAM

- Flash memory is different from RAM because RAM is volatile (not permanent). When power is turned off, RAM loses all its data. Flash can keep its data intact with no power at all. 


## 4.K/M/G byte/bit  2^32=4G
```
1 bit = a 1 or 0 (b)
4 bits = 1 nybble (?)
8 bits = 1 byte (B)
1024 bytes = 1 Kilobyte (KB)
1024 Kilobytes = 1 Megabyte (MB)
1024 Megabytes = 1 Gigabyte (GB)
1024 Gigabytes = 1 Terabyte (TB)
1024 Terabytes = 1 Petabyte (PB)
```


## 5.ascii／unicode  
## 6.补码 ／反码 two’s complement/one’s complement
- 1’s complement of a binary number is another binary number obtained by toggling all bits in it, i.e., transforming the 0 bit to 1 and the 1 bit to 0.
- 2’s complement of a binary number is 1 added to the 1’s complement of the binary number.
```
1's complement of 12 (1100) is 3 (0011)
2's complement of 12 (1100) is 4 (0100)
```
## 7.什么是overflow：-2^31-2^31-1 
2^31−1 values available for positive integers int32

## 8，huffman code 压缩算法

https://www.geeksforgeeks.org/practice-questions-on-huffman-encoding/

## 9，奇偶校验位基本思想：通信差错
- 奇偶校验：利用在信息后面附加一个奇偶校验位来进行校验

## 10， cpu基本知识：
- 三部分构成：算术逻辑单元、控制单元、寄存器单元  
【1】控制单元  
控制单元是整个CPU的指挥控制中心，由指令寄存器IR（Instruction Register）、指令译码器ID（Instruction Decoder）和 操作控制器OC（Operation Controller） 等组成，对协调整个电脑有序工作极为重要。它根据用户预先编好的程序，依次从存储器中取出各条指令，放在指令寄存器IR中，通过指令译码（分析）确定应该进行什么操作，然后通过操作控制器OC，按确定的时序，向相应的部件发出微操作控制信号。操作控制器OC中主要包括：节拍脉冲发生器、控制矩阵、时钟脉冲发生器、复位电路和启停电路等控制逻辑。  

【2】运算单元  
运算单元是运算器的核心。可以执行算术运算（包括加减乘数等基本运算及其附加运算）和逻辑运算（包括移位、逻辑测试或两个值比较）。相对控制单元而言，运算器接受控制单元的命令而进行动作，即运算单元所进行的全部操作都是由控制单元发出的控制信号来指挥的，所以它是执行部件。

【3】存储单元  
存储单元包括 CPU 片内缓存和寄存器组，是 CPU 中暂时存放数据的地方，里面保存着那些等待处理的数据，或已经处理过的数据，CPU 访问寄存器所用的时间要比访问内存的时间短。采用寄存器，可以减少 CPU 访问内存的次数，从而提高了 CPU 的工作速度。寄存器组可分为专用寄存器和通用寄存器。专用寄存器的作用是固定的，分别寄存相应的数据；而通用寄存器用途广泛并可由程序员规定其用途。  

## 11. register 寄存器 ／cache 高速缓存器
1. 寄存器是中央处理器内的组成部份。寄存器是有限存贮容量的高速存贮部件，它们可用来暂存指令、数据和位址。在中央处理器的控制部件中，包含的寄存器有指令寄存器(IR)和程序计数器(PC)。在中央处理器的算术及逻辑部件中，包含的寄存器有累加器(ACC)。 寄存器是CPU内部的元件，寄存器拥有非常高的读写速度，所以在寄存器之间的数据传送非常快。   
2. 内存包含的范围非常广，一般分为只读存储器（ROM）、随机存储器（RAM）和高速缓存存储器（cache）。   
  
3. Cache ：即高速缓冲存储器，是位于CPU与主内存间的一种容量较小但速度很高的存储器。由于CPU的速度远高于主内存，CPU直接从内存中存取数据要等待一定时间周期，Cache中保存着CPU刚用过或循环使用的一部分数据，当CPU再次使用该部分数据时可从Cache中直接调用,这样就减少了CPU的等待时间,提高了系统的效率。Cache又分为一级Cache(L1 Cache)和二级Cache(L2 Cache)，L1 Cache集成在CPU内部，L2 Cache早期一般是焊在主板上,现在也都集成在CPU内部，常见的容量有256KB或512KB L2 Cache。  

总结：大致来说数据是通过内存-Cache-寄存器，Cache缓存则是为了弥补CPU与内存之间运算速度的差异而设置的的部件。

## 12.算数移位(>>) Arithmetic Shift ／逻辑移位(>>>)logical shift, 基本位运算
- 逻辑移位：移位产生的空位由0来补充，比如11100右移移位变为01110  

- 算术左移同逻辑移位。 
  算术右移有两种可选的方案：左边移入的位由0补充，或者由符号位来补充，这两种实现依赖于编译器。11100右移移位结果可能是01110或者11110。
- A Left Logical Shift of one position moves each bit to the left by one. The vacant least significant bit (LSB) is filled with zero and the most significant bit (MSB) is discarded.
- A Right Logical Shift of one position moves each bit to the right by one. The least significant bit is discarded and the vacant MSB is filled with zero.
- A Left Arithmetic Shift of one position moves each bit to the left by one. The vacant least significant bit (LSB) is filled with zero and the most significant bit (MSB) is discarded. It is identical to Left Logical Shift.
- A Right Arithmetic Shift of one position moves each bit to the right by one. The least significant bit is discarded and the vacant MSB is filled with the value of the previous (now shifted one position to the right) MSB.
```
e.g:1010101010，其中[]是添加的位

逻辑左移一位：010101010[0]
算数左移一位：010101010[0]
逻辑右移一位：[0]101010101
算数右移一位：[1]101010101


a = 0011 1100   b = 0000 1101
a&b = 0000 1100

a|b = 0011 1101

a^b = 0011 0001

~a  = 1100 0011

&	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
|	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1
^	按位异或运算符：当两对应的二进位相异时，结果为1
~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 (-a-1)
<<	左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。	a << 2 (*2^2)输出结果 240 ，二进制解释： 1111 0000
>>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数 a >> 2 输出结果 15 ，二进制解释： 0000 1111
```

## 13.并发（concurrency）和并行（parallelism）

前者是逻辑上的同时发生（simultaneous），而后者是物理上的同时发生．  

并发性(concurrency)，又称共行性，是指能处理多个同时性活动的能力，并发事件之间不一定要同一时刻发生。  
  
并行(parallelism)是指同时发生的两个并发事件，具有并发的含义，而并发则不一定并行。  


## 14.进程状态转换图：就绪／执行／阻塞   进程管理与切换  进程（process）和线程（thread）

就绪状态：进程已获得除处理机以外的所需资源，等待分配处理机资源；   

运行状态：占用处理机资源运行，处于此状态的进程数小于等于CPU数；   

阻塞状态： 进程等待某种条件，在条件满足之前无法执行；   

进程和线程都是一个时间段的描述，是CPU工作时间段的描述。一个程序至少有一个进程,一个进程至少有一个线程。一个进程可以包括多个线程。
- 进程，在一定的环境下，把静态的程序代码运行起来，通过使用不同的资源，来完成一定的任务。进程就是包换上下文切换的程序执行时间总和 = CPU加载上下文+CPU执行+CPU保存上下文。
- The primary difference is that threads within the same process run in a shared memory space, while processes run in separate memory spaces.  

## 15.死锁(Deadlock)? 如何解决

- Deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. 

### Deadlock can arise if following four conditions hold simultaneously (Necessary Conditions)  
- Mutual Exclusion: One or more than one resource are non-sharable (Only one process can use at a time)  
- Hold and Wait: A process is holding at least one resource and waiting for resources.  
- No Preemption: A resource cannot be taken from a process unless the process releases the resource.  
- Circular Wait: A set of processes are waiting for each other in circular form.  

死锁产生的四个必要条件

互斥：至少有一个资源必须属于非共享模式，即一次只能被一个进程使用；若其他申请使用该资源，那么申请进程必须等到该资源被释放为止；

占有并等待：一个进程必须占有至少一个资源，并等待另一个资源，而该资源为其他进程所占有；

非抢占：进程不能被抢占，即资源只能被进程在完成任务后自愿释放

循环等待：若干进程之间形成一种头尾相接的环形等待资源关系

### Methods for handling deadlock  
three ways
1) Deadlock prevention or avoidance: The idea is to not let the system into deadlock state.
One can zoom into each category individually, Prevention is done by negating one of above mentioned necessary conditions for deadlock.
Avoidance is kind of futuristic in nature. By using strategy of “Avoidance”, we have to make an assumption. We need to ensure that all information about resources which process WILL need are known to us prior to execution of the process. We use Banker’s algorithm (Which is in-turn a gift from Dijkstra) in order to avoid deadlock.

2) Deadlock detection and recovery: Let deadlock occur, then do preemption to handle it once occurred.

3) Ignore the problem all together: If deadlock is very rare, then let it happen and reboot the system. This is the approach that both Windows and UNIX take.


## 16.What is virtual memory（虚拟内存） and what advantage

- 虚拟内存允许执行进程不必完全在内存中。  
- 虚拟内存的基本思想是：每个进程拥有独立的地址空间，这个空间被分为大小相等的多个块，称为页(Page)，每个页都是一段连续的地址。这些页被映射到物理内存，但并不是所有的页都必须在内存中才能运行程序。当程序引用到一部分在物理内存中的地址空间时，由硬件立刻进行必要的映射；当程序引用到一部分不在物理内存中的地址空间时，由操作系统负责将缺失的部分装入物理内存并重新执行失败的命令。这样，对于进程而言，逻辑上似乎有很大的内存空间，实际上其中一部分对应物理内存上的一块(称为帧，通常页和帧大小相等)，还有一些没加载在内存中的对应在硬盘上   

- Virtual Memory is a storage allocation scheme in which secondary memory can be addressed as though it were part of main memory. The addresses a program may use to reference memory are distinguished from the addresses the memory system uses to identify physical storage sites, and program generated addresses are translated automatically to the corresponding machine addresses.    

## 17.简单了解分布式系统
分布式系统是由一组通过网络进行通信、为了完成共同的任务而协调工作的计算机节点组成的系统。  

A distributed system, also known as distributed computing, is a system with multiple components located on different machines that communicate and coordinate actions in order to appear as a single coherent system to the end-user.

There are two general ways that distributed systems function:   
Each machine works toward a common goal and the end-user views results as one cohesive unit.   
Each machine has its own end-user and the distributed system facilitates sharing resources or communication services.    

### Types of distributed systems   
Distributed systems generally fall into one of four different basic architecture models:  

1. Client-server—Clients contact the server for data, then format it and display it to the end-user. The end-user can also make a change from the client-side and commit it back to the server to make it permanent.
2. Three-tier—Information about the client is stored in a middle tier rather than on the client to simplify application deployment. This architecture model is most common for web applications.
3. n-tier—Generally used when an application or server needs to forward requests to additional enterprise services on the network.
Peer-to-peer—There are no additional machines used to provide services or manage resources. Responsibilities are uniformly distributed among machines in the system, known as peers, which can serve as either client or server.



### 18. OSI七层与TCP/IP五层网络架构详解

（1）OSI七层模型  
OSI中的层 功能 TCP/IP协议族  
应用层 文件传输，电子邮件，文件服务，虚拟终端 TFTP，HTTP，SNMP，FTP，SMTP，DNS，Telnet   
表示层 数据格式化，代码转换，数据加密 没有协议  
会话层 解除或建立与别的接点的联系 没有协议  
传输层 提供端对端的接口 TCP，UDP    
网络层 为数据包选择路由 IP，ICMP，RIP，OSPF，BGP，IGMP   
数据链路层 传输有地址的帧以及错误检测功能 SLIP，CSLIP，PPP，ARP，RARP，MTU  
物理层 以二进制数据形式在物理媒体上传输数据 ISO2110，IEEE802，IEEE802.2  

（2）TCP/IP五层模型的协议  
应用层  
传输层  
网络层  
数据链路层  
物理层  



19，       dns look up 输入google.com发生什么； ftp/ssl/telnet
20，      What is 404 error? 3xx error? 5xx error? http status codes：403，404，400，502
21，       IP v4 4类地址(a, b,c, d). IP v6
22，       什么是html／xml
23，       tcp／ udp ；http／https区别
## 24.什么是病毒／木马／蠕虫？

- 什么是恶意软件？
恶意软件是存在恶意的软件的简称，是用于描述有害软件或入侵性软件的通用词。 我们下面要讨论的一些主题（病毒、勒索软件、蠕虫和特洛伊木马）都属于恶意软件。 


- 什么是病毒(Computer Virus)？
病毒是一种几乎无需用户干预即可进行自我复制的程序。 病毒通常包含一组代码，潜伏一段时间后会引发意外的事件，通常为恶意事件。 这种“恶意负载”可能会破坏数据，或在您的计算机上引发其他类型的问题。 病毒通常会伪装成游戏、其他合法软件或是带有极具吸引力的营销标题的图像，诱使您点击并打开或运行程序。

（1）它必须能自行执行。它通常将自己的代码置于另一个程序的执行路径中。   
（2）它必须能自我复制。例如，它可能用受病毒感染的文件副本替换其他可执行文件。病毒既可以感染桌面计算机也可以感染网络服务器。   

- 什么是勒索软件？
勒索软件是一种能够锁定您的计算机和移动设备或对您的文档、图片和其他重要文件进行加密的恶意软件。 与病毒一样，勒索软件通常会伪装成游戏或其他类型的合法软件。 勒索软件加密您的数据后，通常会勒索赎金。 有时候，支付赎金即可解锁您的文件并恢复访问。 但并不是支付了赎金就一定能够赎回您的数据；许多用户支付了赎金，却没有赎回自己的数据。  


- 什么是蠕虫(worm)？
蠕虫是一种能够在驱动器、计算机和网络中进行自我复制和传播的病毒程序。 蠕虫可通过电子邮件、受感染的网站或即时消息系统等途径将自身副本发送给网络连接中的其他计算机。 部分蠕虫病毒可以按“@m”或“@mm”进行区分，表示他们的主要传播途径是通过电子邮件或群发邮件。 例如 W32 / Klez.e@MM 就是一种群发邮件蠕虫。 蠕虫是一种通过网络传播的恶性病毒，它具有病毒的一些共性，如传播性、隐蔽性、破坏性等等，同时具有自己的一些特征，如不利用文件寄生(有的只存在于内存中)，对网络造成拒绝服务，以及和黑客技术相结合，蠕虫不使用驻留文件即可在系统之间进行自我复制, 蠕虫病毒的传染目标是互联网内的所有计算机.


- 什么是特洛伊木马程序(Trojan horse program)？
特洛伊木马程序（又称特洛伊木马）是一种病毒程序，通常会伪装成或描述成有一组实用或理想功能的程序，但实际上包含破坏性的恶意负载。 特洛伊木马程序不同于一般的病毒，因为它没有复制能力。 但是许多病毒和蠕虫会使用木马程序来感染系统。 特洛伊木马程序不同于一般的病毒，但它们同样极具破坏性。 木马程序潜入人的电脑之中的目的不主要为了破坏你的系统，更是为了获取你的系统中有用的信息，这样就必需当你上网时能与远端客户进行通讯.

许多人使用“特洛伊木马”这一术语来指代不会自我复制的恶意程序， 旨在区分木马程序和病毒。



## 25.翻译过程：词法分析，语法分析和代码生成

- 词法分析（Lexical analysis或Scanning）和词法分析程序（Lexical analyzer或Scanner）
　　词法分析阶段是编译过程的第一个阶段。这个阶段的任务是从左到右一个字符一个字符地读入源程序，即对构成源程序的字符流进行扫描然后根据构词规则识别单词(也称单词符号或符号)。词法分析程序实现这个任务。词法分析程序可以使用lex等工具自动生成。

- 语法分析（Syntax analysis或Parsing）和语法分析程序（Parser）
　　语法分析是编译过程的一个逻辑阶段。语法分析的任务是在词法分析的基础上将单词序列组合成各类语法短语，如“程序”，“语句”，“表达式”等等.语法分析程序判断源程序在结构上是否正确.源程序的结构由上下文无关文法描述.

- 语义分析（Syntax analysis）
　　语义分析是编译过程的一个逻辑阶段. 语义分析的任务是对结构上正确的源程序进行上下文有关性质的审查, 进行类型审查.例如一个C程序片断:
　　int arr[2],b;
　　b = arr * 10;
　　源程序的结构是正确的.
　　语义分析将审查类型并报告错误:不能在表达式中使用一个数组变量,赋值语句的右端和左端的类型不匹配.

Lex
　　一个词法分析程序的自动生成工具。它输入描述构词规则的一系列正规式,然后构建有穷自动机和这个有穷自动机的一个驱动程序,进而生成一个词法分析程序.

Yacc
　　一个语法分析程序的自动生成工具。它接受语言的文法,构造一个LALR(1)分析程序.因为它采用语法制导翻译的思想,还可以接受用C语言描述的语义动作,从而构造一个编译程序. Yacc 是 Yet another compiler compiler的缩写.

源语言（Source language）和源程序（Source program）
　　被编译程序翻译的程序称为源程序,书写该程序的语言称为源语言.

目标语言（Object language or Target language）和目标程序（Object program or Target program）
　　编译程序翻译源程序而得到的结果程序称为目标程序, 书写该程序的语言称为目标语言.

中间语言（中间表示）（Intermediate language(representation)）
　　在进行了语法分析和语义分析阶段的工作之后，有的编译程序将源程序变成一种内部表示形式，这种内部表示形式叫做中间语言或中间表示或中间代码。所谓“中间代码”是一种结构简单、含义明确的记号系统，这种记号系统复杂性介于源程序语言和机器语言之间，容易将它翻译成目标代码。另外，还可以在中间代码一级进行与机器无关的优化。

 

文法（Grammars）
　　文法是用于描述语言的语法结构的形式规则。文法G定义为四元组(，，，)。其中为非终结符号(或语法实体，或变量)集；为终结符号集；为产生式(也称规则)的集合；产生式(规则)是形如或 a ::=b 的(a , b)有序对,其中(∪)且至少含有一个非终结符，而(∪)。，和是非空有穷集。称作识别符号或开始符号，它是一个非终结符，至少要在一条规则中作为左部出现。
　　一个文法的例子: G=(={A，R},={0,1} ，={A?0R，A?01,R?A1},=A)
文法分类（A hierarchy of Grammars）
　　文法的四种类型分别是0型、1型、2型和3型。几类文法的差别在于对产生式施加不同的限制，分别是：
　　0型文法(短语结构文法)(phrase structure grammars)：
　　设G=(，，，)，如果它的每个产生式是这样一种结构： (∪)　　且至少含有一个非终结符，而(∪)，则G是一个0型文法。  
　　1型文法（上下文有关文法）(context-sensitive grammars)：
　　设G=(，，，)为一文法，若中的每一个产生式均满足|，仅仅　　除外，则文法G是1型或上下文有关的。  
　　2型文法（上下文无关文法）(context-free grammars)：
　　设G=(，，，)，若P中的每一个产生式满足：是一非终结符，(∪)　　则此文法称为2型的或上下文无关的。  
　　3型文法（正规文法）(regular grammars)：
　　设G=(，，，)，若中的每一个产生式的形式都是A→aB或A→a，其中A和B都是非终结，a是终结符，则G是3型文法或正规文法。  
　　0型文法产生的语言称为0型语言。   
　　1型文法产生的语言称为1型语言，也称作上下文有关语言。  
　　2型文法产生的语言称为2型语言，也称作上下文无关语言。  
　　3型文法产生的语言称为3型语言，也称作正规语言。

## 26.统一建模语言（uml）

Unified Modeling Language (UML) is a general purpose modelling language. The main aim of UML is to define a standard way to visualize the way a system has been designed. It is quite similar to blueprints used in other fields of engineering.  

UML is linked with object oriented design and analysis. UML makes the use of elements and forms associations between them to form diagrams. Diagrams in UML can be broadly classified as:   

Structural Diagrams – Capture static aspects or structure of a system. Structural Diagrams include: Component Diagrams, Object Diagrams, Class Diagrams and Deployment Diagrams.  
Behavior Diagrams – Capture dynamic aspects or behavior of the system. Behavior diagrams include: Use Case Diagrams, State Diagrams, Activity Diagrams and Interaction Diagrams.  

- Class – A class defines the blue print i.e. structure and functions of an object.    
- Objects – Objects help us to decompose large systems and help us to modularize our system. Modularity helps to divide our system into understandable components so that we can build our system piece by piece. An object is the fundamental unit (building block) of a system which is used to depict an entity.   
- Inheritance – Inheritance is a mechanism by which child classes inherit the properties of their parent classes.  
- Abstraction – Mechanism by which implementation details are hidden from user.  
- Encapsulation – Binding data together and protecting it from the outer world is referred to as encapsulation.  
- Polymorphism – Mechanism by which functions or entities are able to exist in different forms.  



## 27.设计模式23种 简单掌握singleton ／factory





## 28.黑盒／白盒  AB Test

- 黑盒测试：已知产品的功能设计规格，可以进行测试证明每个实现了的功能是否符合要求。
- 白盒测试：已知产品的内部工作过程，可以通过测试证明每种内部操作是否符合设计规格要求，所有内部成分是否以经过检查。 

软件的黑盒测试意味着测试要在软件的接口处进行。这种方法是把测试对象看做一个黑盒子，测试人员完全不考虑程序内部的逻辑结构和内部特性，只依据程序的需求规格说明书，检查程序的功能是否符合它的功能说明。因此黑盒测试又叫功能测试或数据驱动测试。　 

软件的白盒测试是对软件的过程性细节做细致的检查。这种方法是把测试对象看做一个打开的盒子，它允许测试人员利用程序内部的逻辑结构及有关信息，设计或选择测试用例，对程序所有逻辑路径进行测试。通过在不同点检查程序状态，确定实际状态是否与预期的状态一致。因此白盒测试又称为结构测试或逻辑驱动测试。   

- AB Test: a randomized experiment with two variants, A and B
我们的做A/B测试的试验的目的就是推翻2个版本无差异的原假设，验证他们有差异的备择假设。


## 29.数据库基本概念和基本操作
## 30.B＋树／index
## 31.软件生命周期的传统开发阶段：需求分析->设计-> 实现 ->测试
## 32.什么是数据挖掘：聚类分析／关联分析
## 33. 人工智能基础：图灵测试、自然语言处理，A* 算法
## 34. P／Np 问题： TSP问题
## 35. 公钥／私钥： RSA: 证书
公钥（Public Key）与私钥（Private Key）是通过一种算法得到的一个密钥对（即一个公钥和一个私钥），公钥是密钥对中公开的部分，私钥则是非公开的部分。
使用这个密钥对的时候，如果用其中一个密钥加密一段数据，必须用另一个密钥解密。比如用公钥加密数据就必须用私钥解密，如果用私钥加密也必须用公钥解密，否则解密将不会成功。

## 36. Simple Regular Expression, e.g: match valid IP v4 address


Factory, Singleton, Adapter, Composite, Observer(Listener), Template Method, Proxy, Visitor, Iterator. 
如果是临阵抱佛脚的可以多多关注这几个pattern。State，Bridge和Strategy也可以大体看看。
