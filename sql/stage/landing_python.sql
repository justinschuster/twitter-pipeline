-- stage.landing_python definition

-- Drop table

-- DROP TABLE stage.landing_python;

CREATE TABLE IF NOT EXISTS stage.landing_python
(
    edit_history_tweet_ids NUMERIC(20, 0),
    tweet_id NUMERIC(20,0),
    text VARCHAR(256)
);

ALTER TABLE stage.landing_python owner to awsuser;