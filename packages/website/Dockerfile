# Usa la imagen oficial de nginx basada en Alpine para un tamaño más pequeño
FROM nginx:alpine

# Elimina la configuración por defecto de nginx
RUN rm /etc/nginx/conf.d/default.conf

# Copia la configuración personalizada de nginx
COPY nginx.conf /etc/nginx/conf.d/

# Copia los archivos de la aplicación al directorio de nginx
COPY . /usr/share/nginx/html/

# COPY index.html /usr/share/nginx/html/
# COPY reporte.html /usr/share/nginx/html/
# COPY index.js /usr/share/nginx/html/
# COPY reporte.js /usr/share/nginx/html/
# COPY styles.css /usr/share/nginx/html/

# Si tienes un ícono de comida, descomenta esta línea:
# COPY food-icon.png /usr/share/nginx/html/

# Expone el puerto 80
EXPOSE 80

# Comando para iniciar nginx
CMD ["nginx", "-g", "daemon off;"]