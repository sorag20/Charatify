FROM node:14-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN npm install axios

EXPOSE 4000

CMD ["npm", "start"]