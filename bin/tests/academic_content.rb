# Data integrity checks; run with bibtex-ruby, liquid and latex-decode installed.
require 'bibtex'
require 'yaml'
require 'latex/decode'
require 'uri'
bib = BibTeX.open('_bibliography/papers.bib')
entries=bib.entries.values
raise 'Wrong bibliography size' unless entries.size == 27
normalized=entries.map { |e| LaTeX.decode(e.title.to_s).downcase.gsub(/[^a-z0-9]/,'') }
raise 'Duplicate titles' unless normalized.uniq.size == entries.size
counts=entries.group_by{|e|e[:publication_status].to_s}.transform_values(&:size)
raise counts.inspect unless counts == {'Published'=>21,'Preprint'=>3,'Under review'=>3}
entries.each do |e|
  raise "Missing authors: #{e.key}" if e.author.nil? || e.author.empty?
  raise "Missing year: #{e.key}" unless e.year.to_s.match?(/\A20\d{2}\z/)
  raise "Missing source: #{e.key}" unless e[:source]
  if e[:publication_status].to_s=='Under review'
    raise "Unclear review status: #{e.key}" unless e[:note].to_s.include?('Under review, ACL ARR (October 2026)')
  end
end
original_keys=%w[chan2025xtomexploringmultilingualtheory jiayang2025integroundevaluationverificationretrieval]
original_keys.each{|key| raise "Missing original identity #{key}" unless bib[key]}
raise 'Old XToM year' unless bib['chan2025xtomexploringmultilingualtheory'].year.to_s=='2026'
raise 'Old SessionIntentBench year' unless bib['DBLP:journals/corr/abs-2507-20185'].year.to_s=='2026'
raise 'Old RAG title' unless LaTeX.decode(bib['DBLP:journals/corr/abs-2507-09477'].title.to_s)=='A Survey of RAG-Reasoning Systems in Large Language Models'
selected=YAML.load_file('_data/selected_research.yml')
raise 'Expected five focused highlights' unless selected.size==5
selected.each do |paper|
  match=bib[paper['key']]
  raise "Missing selected work: #{paper['title']}" unless match
  raise "Incorrect status: #{paper['title']}" unless match[:publication_status].to_s==paper['status']
  raise "Wrong featured title: #{paper['title']}" unless LaTeX.decode(match.title.to_s)==paper['title']
  position = paper['authorship']=='Second-Author Work' ? 1 : 0
  raise 'Incorrect authorship label' unless match.author[position].last.to_s=='Chan' && match.author[position].first.to_s=='Chunkit'
  if paper['status']=='Under review'
    raise 'Review manuscript needs explicit label' unless paper['venue']=='Under Review'
    raise 'Expected honest internal manuscript link' unless paper['url']=="/publications/##{match.key}"
  else
    raise 'Published link mismatch' unless match.url.to_s==paper['url']
  end
end
profile=YAML.load_file('_data/profile.yml')
raise 'Expected only the three requested HKUST degrees' unless profile['education'].size==3
raise 'Removed bachelor degree remains' if profile['education'].any?{|e|e['degree'].include?('B.Eng.')}
raise 'Mental world models missing' unless profile['research'].any?{|r|r['title'].include?('Mental World Models')}
agents = profile['research'].find{|r|r['title']=='Agents'}
raise 'Missing Agents research direction' unless agents
raise 'Incorrect agent paper' if agents['papers'].any?{|p|p['title']=='From Mind to Action'}
raise 'Missing relevant agent studies' unless agents['papers'].map{|p|p['title']}==['Guandan','NegotiationToM']
post_training=profile['research'].find{|r|r['title'].start_with?('Post-Training')}
raise 'Post-training paper lost' unless post_training['papers'].any?{|p|p['title']=='From Mind to Action'}
raise 'Wrong internship timeline' unless profile['experience'].map{|j|j['dates']}==['Aug 2025 — Present','Feb 2025 — Aug 2025','Mar 2022 — Jan 2025']
raise 'Wrong contact email' unless YAML.load_file('_config.yml')['email']=='ckchancc@connect.ust.hk'
raise 'Phone number leaked' if Dir['_site/**/*.html'].any?{|p|File.read(p).include?('56227926')}
puts 'PASS: 27 deduplicated records, publication statuses, source attribution, 2026 venue updates, featured-paper consistency, CV timeline, education, contact privacy.'

%w[chan2023discourse li2025backdoor li-etal-2024-privlm chan-privacy].each { |key| raise "Removed paper still present: #{key}" if bib[key] }
raise 'Fellowship not first' unless profile['honors'].first['name']=='Hong Kong PhD Fellowship'
raise 'ACL award should be second honor' unless profile['honors'][1]['name']=='ACL Outstanding Reviewers Award'
raise 'Obsolete service awards data' if profile.key?('service_awards')
raise 'NegotiationToM not moved out of ToM card' if profile['research'].first['papers'].any?{|p|p['title']=='NegotiationToM'}
