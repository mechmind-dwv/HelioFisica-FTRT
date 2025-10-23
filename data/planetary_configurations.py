-- Tabla de configuraciones planetarias
CREATE TABLE planetary_configurations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha DATE NOT NULL,
    ftrt_total REAL,
    ftrt_normalized REAL,
    mercury_ftrt REAL,
    venus_ftrt REAL,
    earth_ftrt REAL,
    mars_ftrt REAL,
    jupiter_ftrt REAL,
    saturn_ftrt REAL,
    uranus_ftrt REAL,
    neptune_ftrt REAL
);

-- Tabla de eventos solares
CREATE TABLE solar_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha DATE NOT NULL,
    event_type TEXT,
    magnitude REAL,
    flare_class TEXT,
    cme_speed REAL,
    dst_index REAL
);
