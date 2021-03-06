const path = require('path');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
  devtool: 'eval-source-map',
  module: {
    rules: [
      {
        test: /\.ts(x?)$/,
        exclude: /node_modules/,
        use: [
          {
            loader: 'ts-loader',
          },
        ],
      },
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
      },
      {
        test: /\.(css|scss)$/,
        loader: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: [
            {
              loader: 'css-loader',
              options: {
                sourceMap: true,
              },
            },
            'postcss-loader',
            {
              loader: 'sass-loader',
              options: {
                sourceMap: true,
              },
            },
          ],
        }),
      },
    ],
  },
  entry: {
    site: path.join(__dirname, 'mesolex/static/ts/index.ts'),
    dataSearch: path.join(__dirname, 'mesolex_site/static/mesolex_site/ts/search.tsx'),
  },
  output: {
    path: path.join(__dirname, 'mesolex/static/dist'),
    filename: '[name].bundle.js',
  },
  optimization: {
    splitChunks: {
      name: 'vendors',
      chunks: 'all',
    },
  },
  resolve: {
    extensions: ['.js', '.jsx', '.scss', '.ts', '.tsx'],
    alias: {
      mesolex: path.resolve(__dirname, 'mesolex/static/'),
      lexicon: path.resolve(__dirname, 'lexicon/static/jsx/search/'),
      'query-builder': path.resolve(__dirname, 'query_builder/static/ts/'),
    },
  },
  plugins: [
    new ExtractTextPlugin({
      filename: '[name].bundle.css',
    }),
  ],
};
