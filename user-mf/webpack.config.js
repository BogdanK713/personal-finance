const HtmlWebpackPlugin = require('html-webpack-plugin');
const ModuleFederationPlugin = require('webpack/lib/container/ModuleFederationPlugin');
const path = require('path');

module.exports = {
  entry: './src/index.js',
  mode: 'development',
  devServer: {
    port: 8081,
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
      name: 'userApp',
      filename: 'remoteEntry.js',
exposes: {
  './Login': './src/bootstrap.jsx',
  './Register': './src/bootstrap.jsx',
  './Profile': './src/bootstrap.jsx',
  './Users': './src/bootstrap.jsx',
  './AuthContext': './src/components/AuthContext.jsx'
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
