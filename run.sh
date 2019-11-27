# data is stored in da4:/data/play/developer_migration_data
# 1. extract relevant rows (imported at least one of 4 frameworks)
for i in {0..31}; do zcat c2bPtaPkgPJS.$i.gz | python ~/developer_transition/grep_developers_of_frontend_framework.py > /data/play/developer_migration_data/4frameworks.c2PtabPKG.$i & ; done
wait
# 2. calculate statistics (distribution of usages among developers)
cat /data/play/developer_migration_data/4frameworks.c2PtabPKG*| python author2pkgs_notime.py > /data/play/developer_migration_data/author_num_pkgs
# 3. filter out react + angular,
cat author_num_pkgs | grep 'angular,react$' | cut -d\; -f1 > react_angular.authors
# 4. cluster author, aggregate on commit, save by timeline
cat 4frameworks.c2PtabPKG.{0..31} | python /home/yma28/developer_transition/author2timelineActive.py react_angular.authors > author.time.react.angular.commits
# 5. get basic statistics of # commits distribution of these authors, and selected top 10% of authors
cat author.time.react.angular.commits | cut -d\; -f1 | python /home/yma28/developer_transition/prefilter_authors_with_intensive_commits.py > 10percentauthors.react.angular
# 6. get the result by month for top 10% authors
tail -n+2 author.time.react.angular.commits | python 10percentauthors.react.angular > 10percentByMonth.react.angular
