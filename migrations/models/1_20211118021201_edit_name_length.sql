-- upgrade --
ALTER TABLE "ticker" ALTER COLUMN "name" TYPE VARCHAR(256) USING "name"::VARCHAR(256);
-- downgrade --
ALTER TABLE "ticker" ALTER COLUMN "name" TYPE VARCHAR(64) USING "name"::VARCHAR(64);
