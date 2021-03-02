<TeXmacs|1.99.2>

<style|<tuple|article|old-spacing>>

<\body>
  <\doc-data|<doc-title|Day/night time ratio on
  Earth>|<doc-author|<\author-data|<author-name|TK>>
    \;
  <|author-data>
    \;
  <|author-data>
    \;
  </author-data>>>
    \;
  </doc-data>

  <section|Introduction>

  Here a simplified computation of day and night length along lattitude and
  period of the year.

  <section|Presentation>

  We'll derivate an estimation of day/night length for any location and date
  on Earth, from the following simplified explanation: ``as Earth globe
  self-rotates on itself in about 24h on an axis that is about 23\<degree\>
  from normal to ecliptic plane where it rotates in one year around Sun, day
  is when Sun can be seen in the sky, as on the lighted side, and night when
  Sun goes under the horizon and is hidden by Earth's mass.''

  However simple this explanation is, it is already very powerfull in its
  predictions.

  <section|Computation>

  We'll start by a very simple approximation, and stuff more at each step.

  <subsection|Lighted sphere>

  Lets suppose a sphere (<inactive|<reference|fig1>>), that will model our
  globe Earth.

  <\big-figure>
    <image|code/asymptote/simple-sphere.eps|6cm|||>

    \;
  </big-figure|<inactive|<label|fig1>>>

  If it's lighted by a distant Sun, then half of it is under light
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
    <associate|auto-5|<tuple|1|2>>
    <associate|auto-6|<tuple|5|?>>
    <associate|auto-7|<tuple|2|?>>
    <associate|auto-8|<tuple|6|?>>
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