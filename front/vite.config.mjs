import { defineConfig } from 'vite';

export default defineConfig({
    server: {
        port: 4000,
        open: true,
    },
    publicDir: 'public',
    build: {
        outDir: 'dist',
    },
});
