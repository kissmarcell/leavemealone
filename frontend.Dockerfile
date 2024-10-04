FROM node:20-alpine AS build
WORKDIR /app
COPY frontend/package.json .
RUN npm install
COPY frontend .
RUN npm run build

FROM httpd:2.4
WORKDIR /usr/local/apache2/htdocs
COPY --from=build /app/dist .
