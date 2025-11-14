# Usar nginx como imagen base
FROM nginx:alpine

# Eliminar el archivo de configuración predeterminado de nginx
RUN rm /etc/nginx/conf.d/default.conf

# Copiar el archivo de configuración personalizado de nginx
COPY nginx.conf /etc/nginx/conf.d/

# Copiar los archivos del sitio web al directorio predeterminado de nginx
COPY . /usr/share/nginx/html/

# Exponer el puerto 80
EXPOSE 80

# Comando para ejecutar nginx en primer plano
CMD ["nginx", "-g", "daemon off;"]