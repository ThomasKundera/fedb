<TeXmacs|1.99.2>

<style|article>

<\body>
  <\doc-data|<doc-title|Coriolis effects>|<doc-author|<\author-data|<author-name|TK>>
    \;
  <|author-data>
    \;
  <|author-data>
    \;
  </author-data>>>
    \;
  </doc-data>

  <section|Presentation of the problem>

  Some flatters have difficulties to understand what the Coriolis effect is
  and how it act on various objects on Earth. Lets explain that.

  <section|The system>

  <subsection|The Earth>

  The Earth is a globe of 6371 km in radius rotating at a speed of 1
  revolution per 23h56:04.

  <subsection|Coriolis effect>

  In a rotating system, it's sometime conveniant to use the rotating frame as
  reference to perform dynamic computations. However, this referential is not
  galilean (as it is accelerating by rotation), thus Newton's law of dynamic
  cannot be applied directly. It is however possible to use this referential
  by adding some pseudo-forces (resulting from the inertia effects) to
  objects, in order to take the rotation into account.

  The Corriolis (pseudo-)force is one of them.

  This force exerced on a object in that frame has the following expresison:

  <\equation*>
    <wide|F<rsub|c>|\<wide-varrightarrow\>>=-2m<wide|\<Omega\>|\<wide-varrightarrow\>><around*|(|t|)>\<wedge\><wide|v|\<wide-varrightarrow\>>
  </equation*>

  Where:

  <math|<wide|F<rsub|c>|\<wide-varrightarrow\>>> is the resulting Coriolis
  force vector on the object <math|<around*|[|N|]>>

  <math|m> is the mass of the object <math|<around*|[|kg|]>>

  <math|<wide|\<Omega\><around*|(|t|)>|\<wide-varrightarrow\>>> is the
  rotation vector of the reference frame, in our case, this vector is a
  constant and doesnt depend of time, as Earth rotation speed is (almost)
  constant <math|<around*|[|s<rsup|-1>|]>>

  <math|<wide|v|\<wide-varrightarrow\>>> is the actual speed vector of the
  object <math|<around*|[|m s<rsup|-1>|]>>.

  \;

  In cartesian coordinates, of center <math|O>, center of the Earth, with
  <math|z> axis oriented south-north, we have:
  <math|<wide|\<Omega\>|\<wide-varrightarrow\>>=<matrix|<tformat|<table|<row|<cell|0>>|<row|<cell|0>>|<row|<cell|\<omega\>>>>>>>,
  with <math|w=0.0000727 rad s<rsup|-1>>

  In spherical coordinates, it becomes: <math|<wide|\<Omega\>|\<wide-varrightarrow\>>=<matrix|<tformat|<table|<row|<cell|\<omega\>>>|<row|<cell|0>>|<row|<cell|0>>>>>>,
  notation <math|<matrix|<tformat|<table|<row|<cell|r>>|<row|<cell|\<theta\>>>|<row|<cell|\<varphi\>>>>>>>.

  \;

  \;

  \;

  <section|Application to some concrete cases>

  <subsection|Wind (any air masse, clouds, etc.)>

  Lets supose some volume of air in some air stream. The airflow is parallel
  to the ground and is initially blowing from south to north.

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
    <associate|FigEigthInches|<tuple|6|?>>
    <associate|FigPinHole|<tuple|10|?>>
    <associate|FigShape1|<tuple|1|?>>
    <associate|Fighl|<tuple|9|?>>
    <associate|Figure 1|<tuple|2|?>>
    <associate|SectVanishing|<tuple|3|?>>
    <associate|auto-1|<tuple|1|1>>
    <associate|auto-10|<tuple|2.2.1|2>>
    <associate|auto-11|<tuple|2.5|2>>
    <associate|auto-12|<tuple|3|2>>
    <associate|auto-13|<tuple|3.1|2>>
    <associate|auto-14|<tuple|3.2|2>>
    <associate|auto-15|<tuple|3.2.1|3>>
    <associate|auto-16|<tuple|1|3>>
    <associate|auto-17|<tuple|3.2.2|3>>
    <associate|auto-18|<tuple|3.3|3>>
    <associate|auto-19|<tuple|3.3.1|4>>
    <associate|auto-2|<tuple|2|1>>
    <associate|auto-20|<tuple|3.3.2|4>>
    <associate|auto-21|<tuple|2|4>>
    <associate|auto-22|<tuple|3.4|4>>
    <associate|auto-23|<tuple|3|5>>
    <associate|auto-24|<tuple|3.5|5>>
    <associate|auto-25|<tuple|4|?>>
    <associate|auto-26|<tuple|4.1|?>>
    <associate|auto-27|<tuple|4.2|?>>
    <associate|auto-28|<tuple|4|?>>
    <associate|auto-29|<tuple|4.3|?>>
    <associate|auto-3|<tuple|2.1|1>>
    <associate|auto-30|<tuple|5|?>>
    <associate|auto-31|<tuple|4.4|?>>
    <associate|auto-32|<tuple|6|?>>
    <associate|auto-33|<tuple|4.4.1|?>>
    <associate|auto-34|<tuple|4.4.2|?>>
    <associate|auto-35|<tuple|4.4.3|?>>
    <associate|auto-36|<tuple|4.4.4|?>>
    <associate|auto-37|<tuple|4.4.5|?>>
    <associate|auto-38|<tuple|4.4.6|?>>
    <associate|auto-39|<tuple|7|?>>
    <associate|auto-4|<tuple|2.2|1>>
    <associate|auto-40|<tuple|8|?>>
    <associate|auto-41|<tuple|5|?>>
    <associate|auto-42|<tuple|5.1|?>>
    <associate|auto-43|<tuple|5.2|?>>
    <associate|auto-44|<tuple|9|?>>
    <associate|auto-45|<tuple|5.3|?>>
    <associate|auto-46|<tuple|5.4|?>>
    <associate|auto-47|<tuple|5.4.1|?>>
    <associate|auto-48|<tuple|5.4.2|?>>
    <associate|auto-49|<tuple|10|?>>
    <associate|auto-5|<tuple|3|1>>
    <associate|auto-50|<tuple|5.5|?>>
    <associate|auto-51|<tuple|5.5.1|?>>
    <associate|auto-52|<tuple|11|?>>
    <associate|auto-53|<tuple|13|?>>
    <associate|auto-54|<tuple|13|?>>
    <associate|auto-6|<tuple|3.1|2>>
    <associate|auto-7|<tuple|2|2>>
    <associate|auto-8|<tuple|2.1|2>>
    <associate|auto-9|<tuple|2.2|2>>
    <associate|cite_ref-Lyons_5-2|<tuple|2.2|?>>
    <associate|eq2|<tuple|3.3.2|4>>
    <associate|eqata|<tuple|4|?>>
    <associate|eqd|<tuple|1|?>>
    <associate|eqda|<tuple|1|?>>
    <associate|eqdb|<tuple|3|?>>
    <associate|eqhcircle|<tuple|9|?>>
    <associate|eqhda|<tuple|5|?>>
    <associate|eqhl|<tuple|8|?>>
    <associate|eqhp|<tuple|7|?>>
    <associate|eqhr|<tuple|6|?>>
    <associate|eqmmp|<tuple|10|?>>
    <associate|eqmpr|<tuple|10|?>>
    <associate|figatana|<tuple|5|?>>
    <associate|figflatflat|<tuple|1|?>>
    <associate|fighorizonplot|<tuple|2|?>>
    <associate|figmathorizon|<tuple|1|?>>
    <associate|figspacecurve|<tuple|1|?>>
    <associate|heq|<tuple|9|?>>
  </collection>
</references>

<\auxiliary>
  <\collection>
    <\associate|toc>
      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|1<space|2spc>Presentation
      of the problem> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-1><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|2<space|2spc>The
      system> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-2><vspace|0.5fn>

      <with|par-left|<quote|1tab>|2.1<space|2spc>The Earth
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-3>>

      <with|par-left|<quote|1tab>|2.2<space|2spc>Heliocentric model
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-4>>

      <with|par-left|<quote|2tab>|2.2.1<space|2spc>From horizontal
      coordinates to equatorial coordinates
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-5>>
    </associate>
  </collection>
</auxiliary>