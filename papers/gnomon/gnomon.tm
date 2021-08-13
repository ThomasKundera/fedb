<TeXmacs|1.99.17>

<style|<tuple|article|old-spacing|old-dots|old-lengths>>

<\body>
  <\doc-data|<doc-title|Some simple computations around a
  gnomon>|<doc-author|<\author-data|<author-name|TK>>
    \;
  <|author-data>
    \;
  <|author-data>
    \;
  </author-data>>>
    \;
  </doc-data>

  <section|Introduction>

  A gnomon is a very simple and very old device used to measure the course of
  the Sun in the sky. Easy to build anywhere by anyone (basically one stick
  is enough), it can anyway be used to get quite deep insight about
  astronomical facts.

  <section|Presentation>

  <\big-figure|<image|code/asymptote/simple-gnomon.eps|8cm|8cm||>>
    <inactive|<label|FigGnomon>>
  </big-figure>

  As we can see on Figure <inactive|<reference|FigGnomon>>, a gnomon is a
  simple vertical stick, on a plane surface, such as the shadow of the stick
  summit by the the Sun <math|M<around*|(|x,y,z|)>> is projected on the
  surface as an image <math|M<rprime|'><around*|(|x<rprime|'>,y<rprime|'>,z<rprime|'>|)>>.

  <section|Computation of the projection>

  For a point <math|M<around*|(|x,y,z|)>>,
  <math|M<rprime|'><around*|(|x<rprime|'>,y<rprime|'>,z<rprime|'>|)>> being
  its projection on the gnomon plane, we trivially get <math|z<rprime|'>=-h>,
  where <math|h> is the height of the gnomon stick.

  \;

  We get:

  <math|M<rsub|xy>=<around*|(|x,y,0|)>> and
  <math|M<rsub|xy><rprime|'>=<around*|(|x<rprime|'>,z<rprime|'>,0|)>>

  <math|M<rsub|yz>=<around*|(|0,y,z|)>> and
  <math|M<rsub|yz><rprime|'>=<around*|(|0,y<rprime|'>,h|)>>.

  The triangles <math|M<rsub|xy>M<rsub|y>O> and
  <math|M<rprime|'><rsub|xy>M<rprime|'><rsub|y>O> are homothetics, so:

  <math|OM<rprime|'><rsub|y>/M<rprime|'><rsub|y>M<rprime|'><rsub|yz>=OM<rsub|y>/M<rsub|yz>\<Leftrightarrow\><frac|y<rprime|'>|-h>=<frac|y|z>>

  Same way by projecting on <math|xy> plane will give:

  <math|<frac|x<rprime|'>|-h>=<frac|x|z>>

  \;

  <\equation*>
    <choice|<tformat|<table|<row|<cell|x<rprime|'>=<frac|-hx|z>>>|<row|<cell|y<rprime|'>=<frac|-hy|z>>>|<row|<cell|z=-h>>>>>
  </equation*>

  \;

  For simplicity, as the heigh of the stick is not relevant, only ratio here,
  lest pose <math|h=1>.\ 

  \;

  Thus the projection is:

  <\equation*>
    <choice|<tformat|<table|<row|<cell|x<rprime|'>=<frac|-x|z>>>|<row|<cell|y<rprime|'>=<frac|-y|z>>>|<row|<cell|z=-1>>>>>
  </equation*>

  <section|Computation of projected shapes>

  <subsection|Case of a straight horizontal line>

  <subsection|Case of an horizontal circle above plane>

  <subsection|Case of a circle centered on O>
</body>

<\initial>
  <\collection>
    <associate|page-type|a4>
    <associate|par-hyphen|normal>
  </collection>
</initial>

<\references>
  <\collection>
    <associate|auto-1|<tuple|1|1>>
    <associate|auto-2|<tuple|2|1>>
    <associate|auto-3|<tuple|1|1>>
    <associate|auto-4|<tuple|3|1>>
    <associate|auto-5|<tuple|4|?>>
    <associate|auto-6|<tuple|4.1|?>>
    <associate|auto-7|<tuple|4.2|?>>
    <associate|auto-8|<tuple|4.3|?>>
    <associate|eqmmp|<tuple|3|?>>
    <associate|eqmpr|<tuple|1|?>>
  </collection>
</references>

<\auxiliary>
  <\collection>
    <\associate|figure>
      <tuple|normal|<\surround|<hidden-binding|<tuple>|1>|>
        <mark|<arg|body>|<inline-tag|label|<with|mode|<quote|src>|color|<quote|#228>|font-family|<quote|tt>|figgnomon>>>
      </surround>|<pageref|auto-3>>
    </associate>
    <\associate|toc>
      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|1<space|2spc>Introduction>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-1><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|2<space|2spc>Presentation>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-2><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|3<space|2spc>Computation>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-4><vspace|0.5fn>
    </associate>
  </collection>
</auxiliary>