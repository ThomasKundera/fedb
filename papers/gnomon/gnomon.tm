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
    <label|FigGnomon>
  </big-figure>

  As we can see on Figure <reference|FigGnomon>, a gnomon is a simple
  vertical stick, on a plane surface, such as the shadow of the stick summit
  by the the Sun <math|M<around*|(|x,y,z|)>> is projected on the surface as
  an image <math|M<rprime|'><around*|(|x<rprime|'>,y<rprime|'>,z<rprime|'>|)>>.

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
    <choice|<tformat|<table|<row|<cell|x<rprime|'>=<frac|-x|z>>>|<row|<cell|y<rprime|'>=<frac|-y|z>>>|<row|<cell|z=-1>>>>><eq-number><label|EqProj>*
  </equation*>

  Basically this is a central projection on a plane, nothing new here.

  <section|Computation of projected shapes>

  <subsection|Case of a straight horizontal line>

  We'll take a line parallel to <math|x> axis, at <math|y<rsub|0>> location
  and height <math|h>. So of parametric equation:

  <math|L=<choice|<tformat|<table|<row|<cell|>>|<row|<cell|y=y<rsub|0>>>|<row|<cell|z=h>>>>>>

  We can now use the equation <reference|EqProj> to find it's projection:

  <math|L<rprime|'>=<choice|<tformat|<table|<row|<cell|>>|<row|<cell|y<rprime|'>=<frac|-y<rsub|0>|h>>>|<row|<cell|z=-1>>>>>>

  So, we found that the projection is a straight line also.

  <subsection|Case of an horizontal circle above plane>

  We'll take a circle of center <math|c<around*|(|0,y<rsub|0,h>|)>> and of
  radius <math|r>. So of parametric equation:

  <math|C=<choice|<tformat|<table|<row|<cell|x=r
  cos<around*|(|\<theta\>|)>>>|<row|<cell|y=r
  sin<around*|(|\<theta\>|)>+y<rsub|0>>>|<row|<cell|z=h>>>>>>

  Image of it will be:

  <math|C<rprime|'>=<choice|<tformat|<table|<row|<cell|x=-r
  cos<around*|(|\<theta\>|)>/h>>|<row|<cell|y=-<frac|r
  sin<around*|(|\<theta\>|)>+y<rsub|0>|h>>>|<row|<cell|z=-1>>>>>>

  We also find a circle as image.

  \;

  <subsection|Case of a circle centered on O>

  We'll take a circle of radius r, centered at O, drawn in a plane passing by
  <math|Ox> axis and having a angle with plane <math|xOy> <math|\<alpha\>>.
  It's equation will just be the above circle (equation <reference|EqCprime>)
  shifted by <math|y<rsub|0>>:

  Equation of a circle in <math|xOy> plane:

  <math|C<rsub|1>=<choice|<tformat|<table|<row|<cell|x=r
  cos<around*|(|\<theta\>|)>>>|<row|<cell|y=r
  sin<around*|(|\<theta\>|)>>>|<row|<cell|z=0>>>>>>

  Rotation on <math|Ox> axis by an angle <math|\<alpha\>> has the generic
  form:

  <math|M<rprime|'>=<choice|<tformat|<table|<row|<cell|x<rprime|'>=x>>|<row|<cell|y<rprime|'>=cos<around*|(|\<alpha\>|)>y-sin<around*|(|\<alpha\>|)>z>>|<row|<cell|z=sin<around*|(|\<alpha\>|)>y+cos<around*|(|\<alpha\>|)>z>>>>>>

  Which gives for <math|C<rsub|1>>:

  \;

  <math|C<rsub|>=<choice|<tformat|<table|<row|<cell|x=r
  cos<around*|(|\<theta\>|)>>>|<row|<cell|y=r
  sin<around*|(|\<theta\>|)>cos<around*|(|\<alpha\>|)>>>|<row|<cell|z=r
  sin<around*|(|\<theta\>|)>sin<around*|(|\<alpha\>|)>>>>>><eq-number><label|EqCprime>>

  \;

  So it's image will be:

  <math|C<rprime|'>=<choice|<tformat|<table|<row|<cell|x<rprime|'>=<frac|-r
  cos<around*|(|\<theta\>|)>|r sin<around*|(|\<theta\>|)>sin<around*|(|\<alpha\>|)>>>>|<row|<cell|y<rprime|'>=<frac|-rsin<around*|(|\<theta\>|)>cos<around*|(|\<alpha\>|)>|r
  sin<around*|(|\<theta\>|)>sin<around*|(|\<alpha\>|)>>>>|<row|<cell|z=-1>>>>>=<choice|<tformat|<table|<row|<cell|x<rprime|'>=<frac|-cot<around*|(|\<theta\>|)>|sin<around*|(|\<alpha\>|)>>>>|<row|<cell|y<rprime|'>=-cot<around*|(|\<alpha\>|)>>>|<row|<cell|z=-1>>>>>>

  This is just a line.

  <subsection|Case of a circle centered on a point on <math|y> axis>

  We'll take a circle of radius r, centered at a point
  <math|P<rsub|0><around*|(|0,y<rsub|0>,0|)>>, drawn in a plane containing a
  parallel to <math|Ox> axis passing by <math|P<rsub|0>> and having a angle
  with plane <math|xOy> <math|\<alpha\>>.

  For a circle centered on O, we get (Equation <reference|EqCprime>):

  \;

  <math|C<rsub|1>=<choice|<tformat|<table|<row|<cell|x=r
  cos<around*|(|\<theta\>|)>>>|<row|<cell|y=r
  sin<around*|(|\<theta\>|)>cos<around*|(|\<alpha\>|)>>>|<row|<cell|z=rsin<around*|(|\<theta\>|)>sin<around*|(|\<alpha\>|)>>>>>>>

  Lets now translate it along <math|y> axis to <math|y<rsub|0>>:

  <math|C<rsub|>=<choice|<tformat|<table|<row|<cell|x=r
  cos<around*|(|\<theta\>|)>>>|<row|<cell|y=r
  sin<around*|(|\<theta\>|)>cos<around*|(|\<alpha\>|)>+y<rsub|0>>>|<row|<cell|z=r
  sin<around*|(|\<theta\>|)>sin<around*|(|\<alpha\>|)>>>>>>>

  Image of it will be:

  <math|C<rprime|'>=<choice|<tformat|<table|<row|<cell|x<rprime|'>=<frac|-r
  cos<around*|(|\<theta\>|)>|r sin<around*|(|\<theta\>|)>sin<around*|(|\<alpha\>|)>>>>|<row|<cell|y<rprime|'>=<frac|-rsin<around*|(|\<theta\>|)>cos<around*|(|\<alpha\>|)>-y<rsub|0><rsub|>|r
  sin<around*|(|\<theta\>|)>sin<around*|(|\<alpha\>|)>>>>|<row|<cell|z=-1>>>>>=<choice|<tformat|<table|<row|<cell|x<rprime|'>=<frac|-cot<around*|(|\<theta\>|)>|sin<around*|(|\<alpha\>|)>>>>|<row|<cell|y<rprime|'>=-cot<around*|(|\<alpha\>|)>-<frac|y<rsub|0><rsub|>|r
  sin<around*|(|\<theta\>|)>sin<around*|(|\<alpha\>|)>>>>|<row|<cell|z=-1>>>>>>

  This is a more complex shape.

  Lets rewrite it to make sense of it. We'll pose:

  <math|k=sin<around*|(|\<alpha\>|)>>

  <math|k<rprime|'>=cot<around*|(|\<alpha\>|)>>

  <math|l=<frac|y<rsub|0>|r>>

  <math|l<rprime|'>=<frac|l|k>>

  <math|C<rprime|'>=<choice|<tformat|<table|<row|<cell|x<rprime|'>=<frac|-cot<around*|(|\<theta\>|)>|k>>>|<row|<cell|y<rprime|'>=-k<rprime|'>-l<frac|1<rsub|>|k
  sin<around*|(|\<theta\>|)>>>>|<row|<cell|z=-1>>>>>=<choice|<tformat|<table|<row|<cell|x<rprime|'>=<frac|-cot<around*|(|\<theta\>|)>|k>>>|<row|<cell|y<rprime|'>=-k<rprime|'>-l<rprime|'><frac|1<rsub|>|sin<around*|(|\<theta\>|)>>>>|<row|<cell|z=-1>>>>>>

  Which is at a constant <math|k<rprime|'>>, an <math|x\<leftrightarrows\>y>
  coordinate invertion and a change <math|\<theta\>\<rightarrow\><frac|\<pi\>|2>-\<theta\>>
  the equation of an hyperbola:

  <math|H=<choice|<tformat|<table|<row|<cell|x=<frac|a|cos<around*|(|\<theta\>|)>>>>|<row|<cell|y=b
  tan<around*|(|\<theta\>|)>>>>>>>

  \;

  \;

  \;

  \;

  \;

  \;

  \;

  \;

  \;

  \;

  \;

  \;

  \;

  \;

  \;

  \;

  \;

  \;

  \;

  \;

  \;

  \;

  \;

  <section|WTF>

  \;

  We'll take a circle of radius r, centered at O, drawn in a plane rotated by
  an angle <math|\<alpha\>> on <math|Ox> axis and by an angle <math|\<beta\>>
  on axis <math|Oy>.

  Equation of a circle in <math|xOy> plane:

  <math|C<rsub|1>=<choice|<tformat|<table|<row|<cell|x=r
  cos<around*|(|\<theta\>|)>>>|<row|<cell|y=r
  sin<around*|(|\<theta\>|)>>>|<row|<cell|z=0>>>>>>

  Rotation on <math|Ox> axis by an angle <math|\<alpha\>> has the generic
  form:

  <math|M<rprime|'>=<choice|<tformat|<table|<row|<cell|x<rprime|'>=x>>|<row|<cell|y<rprime|'>=cos<around*|(|\<alpha\>|)>y-sin<around*|(|\<alpha\>|)>z>>|<row|<cell|z=sin<around*|(|\<alpha\>|)>y+cos<around*|(|\<alpha\>|)>z>>>>>>

  Which gives for <math|C<rsub|1>>:

  \;

  <math|C<rsub|2>=<choice|<tformat|<table|<row|<cell|x=r
  cos<around*|(|\<theta\>|)>>>|<row|<cell|y=r
  sin<around*|(|\<theta\>|)>cos<around*|(|\<alpha\>|)>-0>>|<row|<cell|z=rsin<around*|(|\<theta\>|)>sin<around*|(|\<alpha\>|)>+0>>>>>>

  Rotation of <math|><math|C<rsub|2>> on <math|Oy> axis by an angle
  <math|\<beta\>> has the generic form:

  <math|M<rprime|'>=<choice|<tformat|<table|<row|<cell|x<rprime|'>=cos<around*|(|\<beta\>|)>x+sin<around*|(|\<beta\>|)>z>>|<row|<cell|y<rprime|'>=y>>|<row|<cell|z=cos<around*|(|\<beta\>|)>z-sin<around*|(|\<beta\>|)>x>>>>>>

  Which gives for <math|C<rsub|1>>:

  \;

  <math|C<rsub|2>=<choice|<tformat|<table|<row|<cell|x=r
  cos<around*|(|\<theta\>|)>cos<around*|(|\<beta\>|)>+rsin<around*|(|\<theta\>|)>sin<around*|(|\<alpha\>|)>sin<around*|(|\<beta\>|)>>>|<row|<cell|y=r
  sin<around*|(|\<theta\>|)>cos<around*|(|\<alpha\>|)>>>|<row|<cell|z=rsin<around*|(|\<theta\>|)>sin<around*|(|\<alpha\>|)>cos<around*|(|\<beta\>|)>-r
  cos<around*|(|\<theta\>|)>sin<around*|(|\<beta\>|)>>>>>>>

  \;

  \;

  \;

  \;

  \;

  Image of it will be:

  <math|<choice|<tformat|<table|<row|<cell|x<rprime|'>=<frac|-r
  cos<around*|(|\<theta\>|)>|rsin<around*|(|\<theta\>|)>sin<around*|(|\<alpha\>|)>>>>|<row|<cell|y<rprime|'>=<frac|-rsin<around*|(|\<theta\>|)>cos<around*|(|\<alpha\>|)>|r
  sin<around*|(|\<theta\>|)>sin<around*|(|\<alpha\>|)>>>>|<row|<cell|z=-1>>>>>=<choice|<tformat|<table|<row|<cell|x<rprime|'>=<frac|-cot<around*|(|\<theta\>|)>|sin<around*|(|\<alpha\>|)>>>>|<row|<cell|y<rprime|'>=-cot<around*|(|\<alpha\>|)>>>|<row|<cell|z=-1>>>>>>

  This is just a line.

  \;

  \;

  \;

  \;

  \;

  \;
</body>

<\initial>
  <\collection>
    <associate|page-type|a4>
    <associate|par-hyphen|normal>
  </collection>
</initial>

<\references>
  <\collection>
    <associate|EqCprime|<tuple|2|?>>
    <associate|EqProj|<tuple|1|?>>
    <associate|FigGnomon|<tuple|1|?>>
    <associate|auto-1|<tuple|1|1>>
    <associate|auto-10|<tuple|5|?>>
    <associate|auto-2|<tuple|2|1>>
    <associate|auto-3|<tuple|1|1>>
    <associate|auto-4|<tuple|3|1>>
    <associate|auto-5|<tuple|4|?>>
    <associate|auto-6|<tuple|4.1|?>>
    <associate|auto-7|<tuple|4.2|?>>
    <associate|auto-8|<tuple|4.3|?>>
    <associate|auto-9|<tuple|4.4|?>>
  </collection>
</references>

<\auxiliary>
  <\collection>
    <\associate|figure>
      <tuple|normal|<\surround|<hidden-binding|<tuple>|1>|>
        \;
      </surround>|<pageref|auto-3>>
    </associate>
    <\associate|toc>
      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|1<space|2spc>Introduction>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-1><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|2<space|2spc>Presentation>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-2><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|3<space|2spc>Computation
      of the projection> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-4><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|4<space|2spc>Computation
      of projected shapes> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-5><vspace|0.5fn>

      <with|par-left|<quote|1tab>|4.1<space|2spc>Case of a straight
      horizontal line <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-6>>

      <with|par-left|<quote|1tab>|4.2<space|2spc>Case of an horizontal circle
      above plane <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-7>>

      <with|par-left|<quote|1tab>|4.3<space|2spc>Case of a circle centered on
      O <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-8>>

      <with|par-left|<quote|1tab>|4.4<space|2spc>Case of a circle centered on
      a point on <with|mode|<quote|math>|y> axis
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-9>>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|5<space|2spc>WTF>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-10><vspace|0.5fn>
    </associate>
  </collection>
</auxiliary>