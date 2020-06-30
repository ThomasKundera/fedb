<TeXmacs|1.99.2>

<style|<tuple|article|old-spacing>>

<\body>
  <\doc-data|<doc-title|Flat Earth constant
  acceleration>|<doc-author|<\author-data|<author-name|TK>>
    \;
  <|author-data>
    \;
  <|author-data>
    \;
  </author-data>>>
    \;
  </doc-data>

  <section|Introduction>

  Here a simplified computation of a constant accelerating flat Earth.

  <section|Presentation of the problem>

  By equivalence, a <math|9.81ms<rsup|-2>> gravitational field can also be a
  constant acceleration of same value, thus providing a weight on a
  constantly accelerated flat Earth.

  Some opposes that such an acceleration cannot exists, at it would excess
  speed of light in a very short time, which is not possible in Special
  Relativity. But same Special Relativity explains why a constant
  acceleration is possible, as speed don't add.

  <section|Simplified model>

  <subsection|Description>

  To avoid having to solve accelerated referential equations (as it's more
  complex), we'll suppose the following toy model:

  <\itemize-dot>
    <item>From a start platform, a rocket starts, accelerating a a constant
    <math|g=9.81ms<rsup|-2>> rate

    <item>When that rocket reaches <math|v<rsub|o>=c/10> it stops its motors,
    thus becoming an inertia frame of reference

    <item>A secondary rocket, identical to the first, pops from inside the
    first rocket, and immediatly starts accelerating at same <math|g>

    <item>Again, when that rocket reach <math|v<rsub|0>> in the first rocket
    frame, it stops its motors, and another rocket pop out

    <item>Repeat
  </itemize-dot>

  Note: each step is called a ``burst'' in the following.

  <subsection|Things that works>

  Until <math|v<rsub|0>> we can admit to stay more or less in the
  non-relativistic domains: which means that without doing the actual
  relativistic computation, we can assume that a constant acceleration at
  <math|g> from the platform (or subsequent rockets inerta frames) are also
  almost same acceleration as seen from inside the rocket. As time will be
  also about same as in the inertia frame.

  So, for someone in tha always runnig rocket (that would just move from
  rocket to rocket, or just be in the ``last'' one the whole trip), this
  looks like a constant <math|g> acceleration the whole trip.

  So this model is rather cool.

  <subsection|Limitations>

  Of course, that's not exactly the case, and the real acceleration inside
  the running rocket will have to increase in order to keep the apparent
  acceleration in the last inertia frame constant.

  So the actual trip will be a set of increasing acceleration ramps during a
  burst, a sundain decreate of acceleration at burst change, and then a ramp
  up, etc.

  We cannot accurately compute actual time lapses in that accelerating frame
  using our method.\ 

  <section|Computation>

  <subsection|Initial state>

  All computations are done on an <math|x> axis, pointing in the direction of
  the rockets move.

  Notation: All speed, accelerations, times and locations will be labelled as
  such : <math|X<rsub|\<less\>burst sequence number\<gtr\><rsup|\<less\>as
  een from that frame\<gtr\>>>>. For example: <math|v<rsub|8<rsup|2>>> would
  be ``speed of the rocket at end of burst 8, as seen from frame of reference
  2''.

  \;

  Lets place ourself in the ``original'' inertia frame, that we'll call
  <math|R<rsub|0>>.

  In that frame, a rocket accelerates at <math|g> until
  <math|v<rsub|0<rsup|0>>=v<rsub|0>>.

  In <math|R<rsub|0>>, and we have simply:

  <math|t<rsub|0<rsup|0>><rsup|>=t<rsub|0>=v<rsub|0>/g>

  And <math|x<rsub|0<rsup|0>>>, the distance at which the rocket is, that we
  can compute by integrating acceleration:
  <math|x<rsub|0<rsup|0>>=x<rsub|0>=<frac|1|2>gt<rsup|2><rsub|0>>

  At that point, we place ourself in the frame <math|R<rsub|1>> with is in
  linear translation at <math|v<rsub|0>> relative to <math|R<rsub|0>>, with
  an origin at <math|x<rsub|0<rsup|0>><rsup|> >.

  In that frame <math|R<rsub|1>>, we'll also end with a rocket at speed
  <math|v<rsub|1<rsup|1>>=v<rsub|0>>, after a time
  <math|t<rsub|1<rsup|1>>=t<rsub|0>> at a distance
  <math|x<rsub|1<rsup|1>>=x<rsub|0>>.

  <subsection|Lorentz boost to <math|R<rsub|1>>>

  We want to apply a Lorentz transformation to actually know what would the
  rocket trajectory looks like from <math|R<rsub|0>>, now that we know what
  it is in <math|R<rsub|1>>.

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
    <associate|auto-1|<tuple|1|1>>
    <associate|auto-10|<tuple|4.3|?>>
    <associate|auto-11|<tuple|3.3|?>>
    <associate|auto-12|<tuple|4|?>>
    <associate|auto-13|<tuple|4.1|?>>
    <associate|auto-14|<tuple|4.2|?>>
    <associate|auto-15|<tuple|4.3|?>>
    <associate|auto-2|<tuple|2|1>>
    <associate|auto-3|<tuple|3|1>>
    <associate|auto-4|<tuple|3.1|1>>
    <associate|auto-5|<tuple|3.2|2>>
    <associate|auto-6|<tuple|3.3|?>>
    <associate|auto-7|<tuple|4|?>>
    <associate|auto-8|<tuple|4.1|?>>
    <associate|auto-9|<tuple|4.2|?>>
    <associate|figas11|<tuple|1|?>>
    <associate|footnote-1|<tuple|1|?>>
    <associate|footnote-2|<tuple|2|?>>
    <associate|footnote-3|<tuple|3|?>>
    <associate|footnote-4|<tuple|4|?>>
    <associate|footnr-1|<tuple|1|?>>
    <associate|footnr-2|<tuple|2|?>>
    <associate|footnr-3|<tuple|3|?>>
    <associate|footnr-4|<tuple|4|?>>
    <associate|part:code/python/fittable.tm|<tuple|2|?|space_temperature.tm>>
    <associate|part:fittable2.tm|<tuple|4|?|space_temperature.tm>>
  </collection>
</references>

<\auxiliary>
  <\collection>
    <\associate|toc>
      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|1<space|2spc>Introduction>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-1><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|2<space|2spc>Presentation
      of the problem> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-2><vspace|0.5fn>
    </associate>
  </collection>
</auxiliary>