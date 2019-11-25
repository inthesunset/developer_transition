# data is stored in da4:/data/play/developer_migration_data
# 1. extract relevant rows (imported at least one of 4 frameworks)
for i in {0..31}; do zcat c2bPtaPkgPJS.$i.gz | python ~/developer_transition/grep_developers_of_frontend_framework.py > /data/play/developer_migration_data/4frameworks.c2PtabPKG.$i & ; done
wait
# 2. calculate statistics (distribution of usages among developers)
cat /data/play/developer_migration_data/4frameworks.c2PtabPKG*| python author2pkgs_notime.py > /data/play/developer_migration_data/author_num_pkgs
