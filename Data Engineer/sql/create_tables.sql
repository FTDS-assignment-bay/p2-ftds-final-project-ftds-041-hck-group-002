-- =====================================================
-- RAW SCHEMA
-- Table: sales
-- Description:
--     Store raw data imported directly from the source CSV.
-- =====================================================

CREATE TABLE IF NOT EXISTS raw.sales (

    -- Surrogate Key
    id BIGSERIAL PRIMARY KEY,

    -- Source Columns
    date DATE,
    sku VARCHAR(30),
    brand VARCHAR(50),
    segment VARCHAR(50),
    category VARCHAR(50),
    channel VARCHAR(30),
    region VARCHAR(30),
    pack_type VARCHAR(30),

    price_unit NUMERIC(10,2),

    -- Keep the same representation as source (0 / 1)
    promotion_flag SMALLINT,

    delivery_days SMALLINT,

    stock_available INTEGER,

    delivered_qty INTEGER,

    units_sold INTEGER,

    -- Metadata
    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    source_file VARCHAR(255),

    batch_id UUID

);


-- =====================================================
-- ANALYTICS SCHEMA
-- Table: sales
-- Description:
--     Store cleaned and transformed data
--     for analytics and forecasting.
-- =====================================================

CREATE TABLE IF NOT EXISTS analytics.sales (

    -- Surrogate Key
    id BIGSERIAL PRIMARY KEY,

    -- Original Columns
    date DATE,
    sku VARCHAR(30),
    brand VARCHAR(50),
    segment VARCHAR(50),
    category VARCHAR(50),
    channel VARCHAR(30),
    region VARCHAR(30),
    pack_type VARCHAR(30),

    price_unit NUMERIC(10,2),

    promotion_flag SMALLINT,

    delivery_days SMALLINT,

    stock_available INTEGER,

    delivered_qty INTEGER,

    units_sold INTEGER,

    -- Feature Engineering
    year INTEGER,

    month INTEGER,

    quarter INTEGER,

    week_of_year INTEGER,

    day_of_week VARCHAR(15),

    weekend_flag SMALLINT,

    revenue NUMERIC(12,2)

);