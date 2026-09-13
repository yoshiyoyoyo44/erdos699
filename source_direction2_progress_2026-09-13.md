# Erdős 699 — Direction 2 progress only

Date: 2026-09-13

This note records only new progress obtained beyond the previous GitHub state, focused on direction 2: obtaining a uniform upper bound for \(\min(A,B,C)\). It does not claim a proof of the \(i=3\) case or of Erdős Problem 699.

## 1. Compression of the three ratio identity

Using the notation already fixed in the existing work, define
\[
x=\frac{s}{A},\qquad y=\frac{r_B}{B},\qquad z=\frac{r_C}{C},\qquad
\varepsilon=\frac{\delta_1}{ABC}.
\]
Then the established relation becomes
\[
\boxed{x+y+z=\delta+\varepsilon}.
\]
Using \(4r_Br_C=sab\) together with
\[
A^2ab=BCs-\delta_1,
\]
one obtains the additional exact identity
\[
\boxed{4yz=x(x-\varepsilon)}.
\]

Also,
\[
\gcd(s,A)=\gcd(r_B,B)=\gcd(r_C,C)=1.
\]
Thus the three fractions are reduced at the block denominators.

## 2. Explicit unbounded obstruction family for the relaxed system

For every integer \(m\ge0\), define
\[
A=18m+11,\qquad B=144m+85=8A-3,\qquad C=72m+41=4A-3,
\]
\[
a=2,\qquad b=128m+72,\qquad g=8m+5,\qquad h=1,
\]
\[
S=108m+63,\qquad R=3456m^2+4104m+1217,
\]
and
\[
n=2ABC+2,\qquad j=SBg.
\]

Then the following identities hold identically:
\[
\boxed{RS=n-1,}
\]
\[
\boxed{j-1=RAa,\qquad n-j=RCh,\qquad n-j-1=SAb,}
\]
\[
\boxed{BCgh-A^2ab=1.}
\]
Also
\[
\frac n2-j=(18m+11)(3456m^2+3816m+1051)>0,
\]
so \(j<n/2\).

The factors \(A,B,C\) are pairwise coprime, and the relaxed residue assignments hold:
\[
j\equiv1\pmod A,\qquad j\equiv0\pmod B,\qquad j\equiv2\pmod C,
\]
\[
j\equiv1\pmod R,\qquad j\equiv0\pmod S.
\]
Moreover,
\[
n\equiv1\pmod9,
\]
so the family lies in the \(\delta_1=\delta_2=1\) algebraic branch.

Since
\[
\boxed{\min(A,B,C)=A=18m+11\to\infty,}
\]
the presently known relaxed four-factor identities, residue partitions and positivity alone cannot imply a uniform bound for \(\min(A,B,C)\).

The first two cases are
\[
m=0:\quad (n,j)=(76672,26775),\quad (A,B,C)=(11,85,41),
\]
\[
m=1:\quad (n,j)=(1500868,509067),\quad (A,B,C)=(29,229,113).
\]

## 3. Arbitrarily high 2-adic valuation does not remove this relaxed obstruction

For the same family,
\[
\frac n4=P(m)=93312m^3+165240m^2+97497m+19168.
\]
Hence
\[
P(m)\equiv m\pmod2,\qquad P'(m)\equiv1\pmod2.
\]
The elementary 2-adic Hensel lifting criterion gives, for every \(r\ge1\), some integer \(m\ge0\) with
\[
P(m)\equiv0\pmod{2^r}.
\]
Therefore the relaxed family contains members with
\[
\boxed{v_2(n)\ge r+2}
\]
for arbitrarily large \(r\), while \(\min(A,B,C)\) remains unbounded.

Thus even adding an arbitrarily large lower bound on \(v_2(n)\) to the relaxed factor system does not produce a uniform upper bound on the three blocks.

## 4. The obstruction family is not genuinely normalized

For every member of the family,
\[
\boxed{\gcd(n,j)=1.}
\]
Indeed, if an odd prime \(p\mid n,j\), then \(j-1=2AR\) gives \(p\nmid AR\), while \(n-j=RC\) gives \(p\mid C\). But then
\[
n=2ABC+2\equiv2\pmod p,
\]
a contradiction.

For a genuine normalized candidate, \(T\mid n\) and \(T\mid j\), so this family would force \(T=1\). Since \(n\equiv1\pmod9\), the alternative \(n=3\cdot2^u\) is impossible, hence a genuine member would have to satisfy \(n=2^u\).

This cannot occur. Since \(n\equiv1\pmod9\), one would have \(u\equiv0\pmod6\), so \(u-1\) is odd. Every odd prime divisor \(p\mid2^{u-1}-1=ABC\) then has odd \(\operatorname{ord}_p(2)\), hence \((2/p)=1\), so \(p\equiv1\) or \(7\pmod8\). Thus every divisor of \(ABC\), in particular \(B\), must be \(1\) or \(7\pmod8\), whereas
\[
B=144m+85\equiv5\pmod8.
\]
Contradiction.

Therefore this family is an obstruction to overly weak direction-2 arguments, not a counterexample to Erdős 699.

## 5. New unitary-divisor constraint involving the genuine odd part \(T\)

From
\[
\delta_2ABC+1=\gamma T2^{u-1},
\]
put
\[
D=\delta_2BC,\qquad W=\gamma2^{u-1}.
\]
Then
\[
DA+1=TW.
\]
Multiplying
\[
A^2ab+\delta_1=T^2BCgh
\]
by \(D^2\) yields a multiple of \(T^2\):
\[
ab(TW-1)^2+\delta_1D^2\equiv0\pmod{T^2}.
\]
Therefore
\[
\boxed{
ab+\delta_1\delta_2^2B^2C^2
\equiv2TWab\pmod{T^2}.
}
\]
In particular,
\[
\boxed{
T\mid ab+\delta_1\delta_2^2B^2C^2.
}
\]

Let
\[
N=ab+\delta_1\delta_2^2B^2C^2.
\]
Then
\[
\frac NT\equiv2\gamma2^{u-1}ab\pmod T.
\]
Also \(\gcd(T,ab)=1\), \(T\) is odd, and \(\gcd(T,\gamma)=1\). Hence
\[
\boxed{\gcd(T,N/T)=1.}
\]
Equivalently, for every prime power \(p^e\Vert T\),
\[
\boxed{v_p(N)=e.}
\]
Thus
\[
\boxed{
T\text{ is a unitary divisor of }ab+\delta_1\delta_2^2B^2C^2.
}
\]

## 6. Coprimality and size consequences

The four-factor equation also gives
\[
\boxed{\gcd(ab,BC)=1.}
\]
A common prime would divide \(\delta_1\). The only possible prime would be \(3\), but \(\delta_1=3\) implies \(3\nmid Q_2=ABC\).

Using the existing inequality
\[
\delta A>2T^2gh
\]
together with
\[
A^2ab+\delta_1=T^2BCgh,
\]
one gets
\[
\boxed{
ab<\frac{\delta BC}{2A}.
}
\]
Hence along any hypothetical sequence with \(A\to\infty\),
\[
\frac{ab}{BC}\to0.
\]

In the branch \(\delta_1=1\), writing \(U=N/T\), the unitary-divisor relation becomes
\[
\boxed{
TU=ab+(\delta_2BC)^2,\qquad \gcd(T,U)=1.
}
\]

Finally, the already established lower bounds imply
\[
A>\frac{2T^2}{\delta},\qquad
B\ge\frac{T+1}{\delta},\qquad
C>\frac{4T}{\delta},\qquad \delta\le3.
\]
Therefore every genuine candidate satisfies
\[
\boxed{\min(A,B,C)>\frac T3.}
\]
Consequently, any uniform bound \(\min(A,B,C)\le F_0\), if established, would imply \(T<3F_0\).

No uniform constant \(F_0\) is claimed here.
