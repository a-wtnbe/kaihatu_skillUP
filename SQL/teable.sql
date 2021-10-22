-- 右結合する
SELECT * FROM players RIGHT JOIN jobs ON jobs.id = players.job_id ORDER BY players.id;
