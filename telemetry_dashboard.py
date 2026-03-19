if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # ... (todo seu código anterior)

    # Alerts
    st.subheader("Operational Alerts")

    if signal_loss is not None and signal_loss > 10:
        st.warning(f"High signal loss detected: {signal_loss:.2f}%")

    if max_depth > 200:
        st.error("Depth exceeded safe operational limit!")

    # 🔥 3D Visualization (CORRETO AGORA)
    import plotly.graph_objects as go

    if all(col in df.columns for col in ['latitude', 'longitude', 'depth']):
        st.subheader("3D Mission Visualization")

        fig_3d = go.Figure(data=[go.Scatter3d(
            x=df['longitude'],
            y=df['latitude'],
            z=df['depth'],
            mode='lines+markers',
            marker=dict(size=3),
            line=dict(width=4)
        )])

        fig_3d.update_layout(
            scene=dict(
                zaxis=dict(autorange="reversed"),
                xaxis_title='Longitude',
                yaxis_title='Latitude',
                zaxis_title='Depth'
            )
        )

        st.plotly_chart(fig_3d, use_container_width=True)

     # Coverage Analysis
   if all(col in df.columns for col in ['latitude', 'longitude']):
    st.subheader("Mission Coverage Analysis")

    # Criar grid simples
    lat_bins = pd.cut(df['latitude'], bins=10)
    lon_bins = pd.cut(df['longitude'], bins=10)

    coverage = df.groupby([lat_bins, lon_bins]).size().reset_index(name='count')

    coverage_percent = (len(coverage) / (10 * 10)) * 100

    st.metric("Coverage (%)", round(coverage_percent, 2))
