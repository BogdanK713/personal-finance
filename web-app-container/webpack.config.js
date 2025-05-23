const HtmlWebpackPlugin = require('html-webpack-plugin');
const ModuleFederationPlugin = require('webpack/lib/container/ModuleFederationPlugin');
const path = require('path');

module.exports = {
  entry: './src/index.js',
  mode: 'development',
  devServer: {
    port: 8080,
    historyApiFallback: true,
  },
  output: {
    publicPath: 'auto',
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
      }
    ]
  },
  plugins: [
    new ModuleFederationPlugin({
      name: 'container',
      remotes: {
        userApp: 'userApp@http://localhost:8081/remoteEntry.js',
        transactionApp: 'transactionApp@http://localhost:8082/remoteEntry.js',
        analyticsApp: 'analyticsApp@http://localhost:8083/remoteEntry.js',
      },
      shared: {
  react: {
    singleton: true,
    requiredVersion: '^18.0.0',
    strictVersion: false, // <- optional but helps avoid mismatches
  },
  'react-dom': {
    singleton: true,
    requiredVersion: '^18.0.0',
    strictVersion: false,
  },
}

    }),
    new HtmlWebpackPlugin({
      template: './public/index.html',
    }),
  ],
  resolve: {
    extensions: ['.js', '.jsx'],
  }
};
