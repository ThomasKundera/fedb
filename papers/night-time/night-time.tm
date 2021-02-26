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

  <section|Presentation of the problem>

  At any time, the Sun lights about half of the globe. As the axis of
  rotation is not normal to the eciptic plane, different areas get different
  day and night time.

  Our goal is to compute the duration of day and night depending on location.

  We'll make the following assumptions: Earth is a perfect sphere, rotating
  on itself in exactly 24h on a fixed axis, stepping<\footnote>
    To avoid having to consider sidereal/solar day consequences, we'll
    suppose the Earth self-rotates a day without moving, and then steps to
    next location on the orbit.
  </footnote> a constant amount of distance each day on a perfect circular
  orbit around a very distant Sun.
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
    <associate|auto-4|<tuple|4|1>>
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
    <\associate|figure>
      <\tuple|normal>
        AS11-40-5923 (reduced for print)

        <mark|<arg|body>|<inline-tag|label|<with|mode|<quote|src>|color|<quote|#228>|font-family|<quote|tt>|figas11>>>
      </tuple|<pageref|auto-5>>

      <tuple|normal||<pageref|auto-7>>
    </associate>
    <\associate|toc>
      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|1<space|2spc>Introduction>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-1><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|2<space|2spc>Gears>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-2><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|3<space|2spc>Simple
      maths> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-3><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|4<space|2spc>A
      picture> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-4><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|5<space|2spc>Measure>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-6><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|6<space|2spc>Conclusion>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-8><vspace|0.5fn>
    </associate>
  </collection>
</auxiliary>