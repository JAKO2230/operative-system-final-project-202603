CREATE TABLE sistemas_operativos (
    id               SERIAL PRIMARY KEY,
    nombre           TEXT NOT NULL,
    anio             INT  NOT NULL,
    tipo             TEXT NOT NULL,
    descripcion      TEXT DEFAULT '',
    kernel           TEXT DEFAULT '',
    sistema_archivos TEXT DEFAULT ''
);

INSERT INTO sistemas_operativos (nombre, anio, tipo, descripcion, kernel, sistema_archivos) VALUES
    ('UNIX', 1969, 'Tiempo compartido', 'Base fundacional de los sistemas modernos multiusuario, multitarea y filosofía POSIX.', 'Monolítico clásico (C)', 'UFS / SysV FS'),
    ('MS-DOS', 1981, 'Monousuario', 'Sistema monousuario de línea de comandos que estandarizó la arquitectura x86.', 'Monolítico 16-bit', 'FAT12 / FAT16'),
    ('Mac OS', 1984, 'Escritorio', 'Interfaz gráfica pionera que transformó la computación personal de escritorio.', 'Monolítico cooperativo / XNU', 'HFS+ / APFS'),
    ('Linux', 1991, 'Kernel monolítico', 'Núcleo monolítico modular de código abierto que impulsa servidores cloud y contenedores.', 'Monolítico modular', 'ext4 / Btrfs / XFS'),
    ('Windows NT', 1993, 'Kernel híbrido', 'Arquitectura híbrida orientada a objetos con capa de abstracción de hardware (HAL).', 'Kernel Híbrido', 'NTFS / ReFS'),
    ('FreeRTOS', 2003, 'Tiempo real', 'Microkernel determinista diseñado para sistemas embebidos de tiempo real crítico.', 'Microkernel RTOS', 'FAT / LittleFS'),
    ('iOS', 2007, 'Móvil', 'Sistema móvil derivado de Darwin/XNU con alto aislamiento y eficiencia energética.', 'XNU Híbrido (Mach + BSD)', 'APFS cifrado'),
    ('Android', 2008, 'Móvil', 'Plataforma móvil basada en kernel Linux optimizada para dispositivos táctiles y contenedores ART.', 'Linux modificado + Binder', 'ext4 / F2FS');
